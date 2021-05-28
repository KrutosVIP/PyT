import tarfile # Tar lib
import sys, os, json # System Libs

from progress.bar import Bar # Progress Bar
class PkgConf:
    # PKG Builder, main function.
    def run_pkgconf(self, info, pyt):
            args = info.info[15].split(" ")[1:]
            if len(args) < 1: package = "."
            else: package = args[0]
            if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/"))):
                return print("Invalid package path!")
            if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/")):
                config = PkgConf.create_config(package, pyt)
            else:
                with open(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/"), encoding = "utf-8") as c:
                    config = json.load(c)
            if os.path.isfile(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + f"{config['name']}_{config['version']}.tar.gz")):
                os.remove(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + f"{config['name']}_{config['version']}.tar.gz"))
            with tarfile.open(name=os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + f"{config['name']}.{config['version']}.pkg.tar.gz"), mode='x:gz') as tar:
                for obj in os.listdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/"))):
                    tar.add(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/" + obj), arcname = obj)
    # Configure pkg
    def create_config(self, package, pyt):
            print("No config in directory! Generating config:")
            name = None
            while name == None:
                try:
                    name = input("Input Package Name>")
                except:
                    pass
            creator = None
            while creator == None:
                try:
                    creator = input("Input Creator>")
                except:
                    pass
            version = None
            while version == None:
                try:
                    version = input("Version>")
                except:
                    pass
            dependencies = None
            while dependencies == None:
                try:
                    dependencies = input("Dependencies(write with spaces)>")
                except:
                    pass
            if not os.path.isdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/")):
                os.mkdir(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/"))
            with open(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/"), "w", encoding = "utf-8") as c:
                json.dump({"name": name, "creator": creator, "version": version, "dependencies": dependencies}, c)
            return {"name": name, "creator": creator, "version": version, "dependencies": dependencies}

    # PKG Config Wrapper
    def configure_wrap(self, package, pyt):
        if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/")):
            config = PkgConf.create_config(self, package, pyt)
        else:
            with open(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/temp/config.json").replace("//", "/"), encoding = "utf-8") as c:
                config = json.load(c)
        return config


    # Build PKG
    def buildpkg(self, info, pyt, package, config, path = None):
            if path == None: path = os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/"))
            if os.path.isfile(os.path.abspath(ppath+ "/" + f"{config['name']}_{config['version']}.tar.gz")):
                os.remove(os.path.abspath(path+ "/" + f"{config['name']}_{config['version']}.tar.gz"))
            with tarfile.open(name=os.path.abspath(path+ "/" + f"{config['name']}.{config['version']}.pkg.tar.gz"), mode='x:gz') as tar:
                for obj in os.listdir(os.path.abspath(path+ "/" + package.replace("\\", "/"))):
                    tar.add(os.path.abspath(path+ "/" + package.replace("\\", "/") + "/" + obj), arcname = obj)

class RepoBuild:
    # Repo Builder
    def run_repobuild(self, info, pyt): # Main Function
        args = info.info[15].split(" ")[1:]
        if len(args) < 1: package = "."
        else: package = args[0]
        if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/"))):
            return print("Invalid repo path!")
        if not os.path.exists(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/repo.json").replace("//", "/")):
            config = RepoBuild.repoconfigure(self, info, package, pyt)
        RepoBuild.repobuild(self, info, pyt, package)

    # Configure packages in repo
    def pkgconf(self, pyt, package, path):
        size = len([filename for filename in os.listdir(path) if os.path.isdir(os.path.join(path, filename))]) # Size of repo in dirs.
        dir = os.listdir(path)[0] # First PKG in dir
        p = Bar(f'{dir}>', max=int(size), fill = "#", suffix='%(percent)d%%') # Create Bar
        configs = {}
        for dir in os.listdir(path):
            if os.path.isdir(os.path.abspath(path + f"/{dir}")):
                print(f"[INFO] Configuring {dir}")
                # Path to main repo
                path2 = os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + dir.replace("\\", "/"))
                config = PkgConf.configure_wrap(self, package, pyt) # Check if it has config, if no - create and get, if yes - get config
                configs.update({dir: config})
                p.next(1)
        p.finish()

        return configs

# Repo Build Process
    def repobuild(self, info, pyt, package):
        repos = ["base", "dev", "kernel", "software"] # Repos

        # Gettin` dirs
        for repo in repos:
            print(f"[INFO] Building repo {repo}")
            path = os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + f"/{repo}").replace("//", "/")
            if os.path.exists(path): # Check if repo exists
                if len(os.listdir(path)) > 1: # Check if there is packages
                    # Get number of packages
                    size = len([filename for filename in os.listdir(path) if os.path.isdir(os.path.join(path, filename))])
                    # Get first PKG in dir
                    pkg = os.listdir(path)[0] 
                    # Configure packages
                    RepoBuild.pkgconf(self, pyt, package, path)

                    # Progress Bar
                    p = Bar(f'{pkg}>', max=int(size), fill = "#", suffix='%(percent)d%%')
                    for pkg in os.listdir(os.path.abspath(path)):
                        if os.path.isdir(os.path.abspath(path + f"/{pkg}")):
                            pkg2 = f"{repo}/{pkg}"
                            p.next(1)
                            try:
                                if not os.path.isdir(os.abspath(repo + "/build")):
                                    os.mkdir(os.abspath(repo + "/build"))
                                PkgConf.buildpkg(self, info, pyt, pkg, configs[pkg], path = os.abspath(repo + "/build")) # Build pkg
                            except:
                                pass
                        p.finish()

    def repoconfigure(self, info, package, pyt):
        print("No repo config in directory! Generating config:")
        name = None
        while name == None:
            try:
                name = input("Input Repo Name>")
            except:
                pass
        creator = f"{pyt.info['user']}@{info.info[8]}"

        version = None
        while version == None:
            try:
                version = input("Build time>")
            except:
                pass
        repo = None
        while repo == None:
            try:
                repo = input("repo url>")
            except:
                pass
        with open(os.path.abspath(pyt.fs[1].replace("\\", "/") + "/" + package.replace("\\", "/") + "/repo.json").replace("//", "/"), "w", encoding = "utf-8") as c:
            json.dump({"name": name, "buildmachine": creator, "btime": version, "repo": repo}, c)
        return {"name": name, "buildmachine": creator, "btime": version, "repo": repo}
