#redirector function
def redirect(command):
        args = command.split(" ")[1:]
        if len(args) > 1:
            if ">" in args:
                args_2 = command.split(">")
                args_2 = [args_2[0], "".join(args_2[1:])]
                args = os.path.splitext(args_2[1])

                args = slugify(args[0]) + "." + slugify(args[1])
                return True, args.replace(" ", ""), args_2[0]
        return False, None, None
            
# Redirector write
def redirect_write(stdout, file):
    with open(file, "w", encoding = "utf-8") as f:
            f.write("".join(stdout.stdout).replace("\n", ""))
