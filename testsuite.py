import subprocess

my_exec = "../build/42sh"
exec_test = "bash"
list_test = [
 [["-c", "ls"], "42sh -c ls"],
 [["--ast-print -c", "ls"], "42sh --ast-print -c ls"]
]
size = max(len(arg[1]) for arg in list_test) + 8


def test(my_exec, exec_test, arg_list, com):
  my_list = [my_exec]
  test_list = [exec_test]
  for arg in arg_list:
    my_list.append(arg)
    test_list.append(arg)
  my = subprocess.run(my_list, stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)

  ref = subprocess.run(test_list, stdout=subprocess.PIPE,
      stderr=subprocess.PIPE)
  com = com + " : "
  while(len(com) < size):
    com = com + " "
  com = com + "{}"
  print(com.format(my.stdout == ref.stdout
        and my.stderr == ref.stderr
        and my.returncode == ref.returncode))


for arg in list_test:
  test(my_exec, exec_test, arg[0], arg[1])
