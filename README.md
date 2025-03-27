# Formal Languages Activity 2

🤝🏻 __Team:__ 🤝🏻 Nathalia Valentina Cardoza Azuaje & Alyson Dahiana Henao Fernandez

📖 __Student’s class number:__ 📖 7309

👾 __Versions:__ 👾
- Operating system: Python 3.12 (64-bit)
- Programming Language: Python
- Tools used in implementation: Visual Studio Code (Version 1.97.2)

👩🏻‍💻 __Detailed instructions for running our implementation:__ 👩🏻‍💻
- Download and install Visual Studio Code on your computer. Once installed, add the Python extension to Visual Studio Code, once installed the Python extension then install in the console the 'nltk' library. Next, download the provided file and open it within the Visual Studio Code environment. Finally, run the uploaded code to complete the process.

🗣️ __Explanation of the algorithm:__ 🗣️
- This algorithm generates and analyzes strings of the form a^n b^n (equal numbers of 'a's followed by equal numbers of 'b's). It consists of several key functions as accepted_strings that generates valid strings of the form a^n b^n by randomly creating strings with equal numbers of 'a's and 'b's and adds them to a list, by rejected_strings that generates random strings from the alphabet a, b and adds them to a list if they do not have an equal number of 'a's and 'b's, the pda_M simulates a PDA that processes the strings and checks if they follow the given form and uses a stack to match each 'a' with a 'b' and accepts or rejects strings based on this condition, the tree is for accepted strings because it generates and prints derivation trees using a CFG illustrating how each string is derived, and last but not least, sf_c tracks the sentential form and stack configuration for each string processed by the PDA printing the changes in the stack and string at each step.
