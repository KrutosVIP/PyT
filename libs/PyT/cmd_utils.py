import sys, os, json
def file_exec(self, redirect, PTSTD, u_i, execute, executable, parse):
    # Check if file executable
    file_exc, execute_var = executable(self, parse[0])
    # Check if we redirecting
    redir, file, args = redirect(u_i)
    # If exec
    if execute_var:
        # Check if redirecting
        if redir == True:
            # Writing all STD to our STD
            sys.stdout = PTSTD()
        # Execute file
        execute(self, file_exc)

        # End redirect
        if redir == True:
            try:
                # Redirecting given output
                redirect_write(sys.stdout, file)
                # Recreating std.
                std2 = sys.stdout
                sys.stdout = std2.basesys
                return True, sys.stdout
            except Exception as e:
                traceback.print_exc()
        return True, sys.stdout
    return False, sys.stdout

def cmd_exec(self, parse, info, u_i, PTSTD, redirect, STDLib):
    if parse[0] in info[10]:
        redir, file, args = redirect(u_i) 
        if redir == True:
            sys.stdout = PTSTD()
            u_i = args
            parse = u_i.split(" ")
                            
        if os.path.exists(f"{info[14].basefs}/../data/{self.info['user']}/.history"):
            with open(f"{info[14].basefs}/../data/{self.info['user']}/.history") as f:
                history = json.load(f)
        else:
            history = {"history": []}

        history["history"].append({parse[0]: "".join(parse[1:])})
        with open(f"{info[14].basefs}/../data/{self.info['user']}/.history", "w") as f:
            history = json.dump(history, f)
                            
        info2 = info.copy(); info2.append(u_i)
        stdlib = STDLib(info2)
        info[10][parse[0]].info["run"](stdlib, self)

        if redir == True:
            try:
                redirect_write(sys.stdout, file)
                std2 = sys.stdout
                sys.stdout = std2.basesys
                del std2
            except Exception as e:
                traceback.print_exc()
        return True
    else:
        return False
