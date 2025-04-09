# pylint: skip-file
from os import environ, system
from build import build

system("clear")
# joe = system("cat /tmp/updated.txt")
# if joe != 0:
#     system("./fix.sh")
# system("clear")
print("Should be nothing from here")
import package.src.firepup650 as fp

print("Until here (Half-second sleep)")
fp.sleep(0.5)
bob = fp.menu({"Yes": "Y", "No": ""}, "(If owner) Build?")
system("clear")
if environ["REPL_OWNER"] == "Firepup650" and bob == "Y":
    build()
    exit()
else:
    print(
        fp.menu(
            {
                "a": "hi",
                "Some fairly long second test case": ["a", "b", "c"],
                "A third test": 0,
            },
            "Test menu",
        )
    )
    fp.console.warn("Test Warning")
    fp.e("No demo yet!")
