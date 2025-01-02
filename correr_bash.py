import subprocess


file_name = "bash_example.sh"
script = ""
#abro el archivo en modo escritura 
#modo rb devuelve un binario y modo r devuelve un string
with open(file_name, "r") as bash_file:
    script = bash_file.read()
    
print(f"Contenido del archivo bash: {script}\n")

subprocess.call(script, shell=True)