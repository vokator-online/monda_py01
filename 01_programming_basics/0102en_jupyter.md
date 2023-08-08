# Jupyter Notebook experimental environment integration with VS Code

## Introduction

Jupyter Notebook is an open-source web application that allows users to create and share documents that contain live code, equations, visualizations, and narrative text. It provides an interactive computing environment where you can write and execute code, view the output, and add explanatory text in Markdown format.

Using Jupyter Notebook in VS Code as an experimental environment offers several benefits:

1. Interactivity: Jupyter Notebook allows you to execute code cells individually, making it easier to test and debug code. You can modify and rerun specific parts of your code without executing the entire script, enabling faster development.

2. Visualization: Jupyter Notebook supports the creation of interactive visualizations, graphs, and charts. You can include images, videos, and rich media to provide a more immersive and engaging experience. 

3. Documentation: Jupyter Notebook combines code execution with narrative text, allowing you to create detailed documentation within the same environment. This makes it easier to explain your thought process, annotate code, and provide comments or instructions.

4. Easy to explore and experiment: With Jupyter Notebook, you can explore data and experiment with different approaches more easily. You can run code cells out of order, manipulate data in real-time, and quickly iterate on different ideas. This flexibility makes it a valuable tool for data analysis, machine learning, and prototyping.

On the other hand, there are a few cons to consider when comparing Jupyter Notebook to regular .py files:

1. Lack of structure: Jupyter Notebook allows for a more ad-hoc and exploratory coding style, which can lead to unstructured and messy code. It may be more challenging to refactor and organize code compared to traditional .py files.

2. Version control issues: Since Jupyter Notebook files are stored in JSON format and contain both code and output, it can result in conflicts and difficulties when using version control systems like Git. Regular .py files are typically easier to manage in version control.

3. Reproducibility challenges: Jupyter Notebook's interactivity and the ability to execute code cells in any order can make reproducing specific results more difficult. It's important to keep track of the execution order of cells and ensure code dependencies are correctly accounted for.

4. Performance limitations: Jupyter Notebook may have performance limitations when dealing with large datasets or computationally intensive tasks. Using regular .py files executed in a traditional Python environment can offer better performance and efficiency for certain tasks.

5. Limited IDE features: While Jupyter Notebook provides a rich environment for code execution and documentation, it may lack some of the advanced IDE features available in dedicated Python IDEs like Visual Studio Code. This can include advanced debugging tools, code refactoring capabilities, and integrated linting or formatting tools. When using Jupyter Notebook integrated into Visual Studio Code, these issues are mostly compensated.

In summary, using Jupyter Notebook as an experimental environment in VS Code can provide interactive, visual, and collaborative features that are beneficial for data exploration, prototyping, and documentation. However, it may have limitations in terms of code structure, version control, performance, and advanced IDE features. Choosing between Jupyter Notebook and regular .py files depends on the specific use case and requirements of your project.

# Installation and VS Code integration

To set up Jupyter Notebook in the VS Code IDE, follow these steps:

1. Install the Jupyter extension: Open VS Code, go to the Extensions view (`Ctrl+Shift+X`/`Cmd+Shift+X` or `View` > `Extensions` in menu) and search for `Jupyter`. Install the Jupyter extension if not yet installed with Python.

1. Create a new Jupyter Notebook: Open the Command Palette (`Ctrl+Shift+P` or `View` > `Command Palette`) and search for `Jupyter: Create New Blank Jupyter Notebook`. Select this option to create a new Jupyter Notebook file. Alternatively, you can just create an empty file in the File Browser and name it with extension `.ipynb`.

1. Select a kernel: After creating a new Notebook, you will be prompted to select a kernel. Choose your recently created virtual environment (`venv`) ![Kernel Selection](img/jupyter_kernel.png) and if prompted, allow access through Windows Firewall.

1. Execute code cells: In the newly created Jupyter Notebook, you can start writing and executing code cells with Ctrl+Enter shortcut or just pressing the triangle button on the left side of the code cell. Each code cell can be executed independently, and the output of the last code line will be displayed below the cell.
![Jupyter Code Cell](img/jupyter_code_cell.png)

1. You will be prompted to install Interactive Python and Jupyter modules into your Python Virtual Environment, if they are not yet there. Choose `Install` option. It may take some time, it may fail. In case of failure or error, you can retry by executing command `pip install ipykernel` in the Terminal, but first make sure virtual environment is activated.
![Manual ipykernel installation](img/manual_ipykernel_installation.png)
After successfull installation, your code cell will execute flawlessly and result will be outputed.

1. Additional features: The Jupyter extension in VS Code provides various features such as code autocompletion, code formatting, and debugging capabilities. You can access these features through the VS Code interface to enhance your Jupyter Notebook experience.

1. Saving and sharing: You can save your Jupyter Notebook just like any other file in VS Code. It will be saved with a .ipynb extension. You can also share the .ipynb file with others, and they can open and run it in their own Jupyter Notebook environment.

1. Notebook kernels: Jupyter Notebook supports multiple programming languages through different kernels. You can change the kernel associated with a notebook using the Kernel menu in the toolbar. This allows you to work with languages other than Python, such as R or Julia.

---

## Chicken or Egg problem: 🐔?🥚

Most of the content below now will not make sens to you yet, but this knowledge will be essential for you later in practice. Just remember to come back here to recap once you will actually start using Jupyter Notebook in VS Code.

---

## Restarting the Kernel

While working in a Jupyter Notebook, sometimes the kernel (the execution environment) can hang or become unresponsive. In VS Code, you can quickly restart the kernel by:

- Clicking the `Restart`/`Restart Kernel` button (usually represented by a circular arrow) at the top of the notebook interface.
![Visual clue where is Restart button](img/jupyter_restart_kernel.png)

- Using the Command Palette (`Ctrl+Shift+P` or `View > Command Palette`) and selecting `Jupyter: Restart Kernel`.

Restarting the kernel can resolve issues related to variable conflicts, stuck computations, and more.

## Displaying line numbers in code cells.

It is sometimes convenient, especially in large code blocks, to have line numbers visible by the code line. However, please be careful not to consider them as a part of the code. You can turn on Line Numbers from extended Jupyter toolbar menu (`...`) just right of that `Restart` button.
![Jupyter Line Numbers toggle](img/jupyter_line_numbers.png)

## Displaying Image and Visualization Libraries

Jupyter Notebook supports integration with popular Python visualization libraries like Matplotlib, Seaborn, Plotly, and more. When you generate plots or visualizations using these libraries in a Jupyter Notebook within VS Code, the outputs are rendered inline below the code cells. This makes it easy to see the results of your data analysis and visualization efforts in real-time. It will prove essential in our data science course.

## Variable Explorer and Data Viewer

The Jupyter extension for VS Code includes a variable explorer and a data viewer. This allows you to inspect the values of variables, dataframes, and other data structures within your notebook. It's an excellent tool for quickly understanding the shape and contents of your data. 

To access the variable explorer, in the extended Jupyter toolbar menu (`...`) just right of that `Restart` button, there is also `Variables` option.
![Jupyter Variable Explorer toggle](img/jupyter_variable_explorer.png)

## Debugging Jupyter Code Cells

VS Code allows for debugging Jupyter code cells, making it easier to troubleshoot issues in your notebook. To start debugging:

Click on the `Debug Cell` icon (usually represented by a bug and play icon combined) in the top left of a code cell.
The debugger will start, and you can set breakpoints, inspect variable values, and step through the code.

## Keyboard Shortcuts in Jupyter

There is a good article clearly explaining the [Jupyter keyboard shortcuts](https://towardsdatascience.com/jypyter-notebook-shortcuts-bf0101a98330), and all of them work in VS Code environment.

## Conclusion

Integrating Jupyter Notebook within the VS Code environment provides a potent combination of interactivity, visualization, and the robust features of a professional IDE. Whether you're analyzing data, building machine learning models, or just prototyping some ideas, this setup can enhance your productivity and streamline your development process.
