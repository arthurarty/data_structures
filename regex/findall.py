import re


def test_email(email):
    x = re.match('([a-zA-Z0-9]+)([.]*)([-]*)([a-zA-Z0-9]+)@{1}([a-z]+)\.([a-z]+)', email)
    print(x)

# test_email("arthur.nangai@gmail.com")
# test_email("arthur@gmail.com")
# test_email("arthur83@gmail.com")
# test_email("arthur-nangai@gmail.com")

str = "test"
print(re.match('[t][e][s][t]([_]+)', str))
