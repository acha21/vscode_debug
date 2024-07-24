
def main():
    
    with open("inline_cmd_options.txt", "r") as f:
        lin = f.read()    
    
    output = []
    for token in lin.strip().split():
        token = token.strip()    
        if token != "":
            if token.startswith('"'):
                token = '\\' + token + '\\'
            if token.startswith("-"):
                if len(output) == 0:
                    output.append(f'"{token}",')
                else:
                    output.append(f'\n"{token}",')
            else:
                output.append(f'"{token}",')
    
    outstr = "".join(output)
    print("-------------------")
    print(outstr[:-1])

if __name__ == "__main__":
    main()
