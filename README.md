


<h1 align="center">
📖 ft_stockholm - 42 Cibersecurity
</h1>

<p align="center">
	<b><i>Little wannacry</i></b><br>
</p>

<p align="center">
	<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Falitomal/ft_stockholm?color=lightblue" />
	<img alt="Code language count" src="https://img.shields.io/github/languages/count/Falitomal/ft_stockholm?color=yellow" />
	<img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Falitomal/ft_stockholm?color=blue" />
	<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Falitomal/ft_stockholm?color=green" />
</p>


## 💡 About the project

```
Features
It only searches for files to encrypt in the /home/user/infection folder.
The encrypted file extensions will be the same as those used by WannaCry.
Decrypted files will either remain in their original folder or be moved to a specified location.
After encrypting the files, the encryption key is stored in clave.key, in the stockholm.py path, for use with the
option when decrypting.
```
## 🛠️ Mandatory
```
When developing mining, three things must be done:
- Calculate the proof of work
- Rewarding the miners (a transaction)
- Create the new block and add it to the chain.
Once the blockchain is created, it will be possible to interact with it through different HTTP requests:
- [POST] /transactions/new : Sends a new transaction to add to the next block.
- GET] /mine : Executes the proof of work and creates a new block.
- GET] /chain : Returns information about the blockchain (blocks, tran- sactions, etc).


```
## 🛠️ Usage
```
```

To use the Stockholm program, follow the instructions below:

Clone the repository and navigate to the project directory.

Ensure you have Python and the required modules installed.

Run the program with the following command:

shell
Copy code
python stockholm.py [options]
Available options:

-v or --version: Show the version of the program.
-r keyfile or --reverse keyfile: Decrypt files using the specified keyfile.
-s or --silent: Run the program in silent mode, without producing any output.
-e extension or --ext extension: Rename files with the specified extension (default: ".ft").
-p folder or --path folder: Specify the folder to encrypt/decrypt files (default: DEFAULT_DIR).
Note: Replace stockholm.py with the actual filename of the program.

Follow the appropriate examples below to perform specific actions:

Encrypt all files in the infection folder:

```
python stockholm.py
Decrypt files in the infection folder using a keyfile:
```
```
python stockholm.py -r keyfile
Decrypt files in the infection folder and store them in a different path:
```
```
python stockholm.py -r keyfile -p /path/to/decryption/folder
Run the program in silent mode, without producing any output:
```
```
python stockholm.py -s
Specify a different file extension for renaming files:
```
```
python stockholm.py -e .newext
Show the version of the program:
```
```
python stockholm.py -v
Please refer to the provided examples and adjust the commands according to your specific requirements.
```
```
