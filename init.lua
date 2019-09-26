-- TODO: remove with update to rpm 4.15 which includes rpm.execute:
-- https://github.com/rpm-software-management/rpm/commit/18e792340e33eade01967d01d5801f1ae9e0ad33
function rpm.execute(path, ...)
  local pid = posix.fork()
  if pid == 0 then
     posix.exec(path, ...)
     io.write(path, ": exec failed: ", posix.errno(), "\n")
     os.exit(1)
  end
  if not pid then
     error(path .. ": fork failed: " .. posix.errno() .. "\n")
  end
  posix.wait(pid)
end
--
