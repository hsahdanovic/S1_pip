import os

def analyze_log_file(filename: str, keyword: str):
    f = open(filename)
    content = f.readlines()
    
    c = set()
    for line in content:
        if keyword.upper() in line.upper():
            c.add(line)

    cname = os.path.splitext(os.path.basename(filename))[0] + "_" + keyword.upper() + "_expected.log"
    
    o = open(cname, "a")
    o.writelines(c)
    print(f"Output: {len(c)}")
    return "Expected content of output file in " + cname
        

if __name__ == "__main__":
    keyword= "ERROR"
    print(analyze_log_file("a7_ex1.log", keyword))

    keyword = 'WARNING'
    print(analyze_log_file("a7_ex1.log" , keyword))

    keyword = 'WARNING'
    print(analyze_log_file("missing.log" , keyword))
