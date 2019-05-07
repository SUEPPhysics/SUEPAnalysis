import submitter as sub

def main():
    job = sub.parallel()
    job.run("echo ", ["-e", "'Running somthing here ... '"], "dummy")

if __name__ == "__main__":
    main()
