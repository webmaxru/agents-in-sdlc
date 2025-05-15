# Exercise 2 - Providing context to Copilot with instruction files

Context is key across many aspects of life, and when working with generative AI. If you're performing a task which needs to be completed a particular way, or if a piece of background information is important, we want to ensure Copilot has access to that information. We can use [instruction files](https://code.visualstudio.com/docs/copilot/copilot-customization)to provide guidance to Copilot not only knows what we want it to do but how we want it to do it.

In this exercise, you will learn:

- how to provide Copilot with project-specific context, coding guidelines and documentation standards using custom instructions (.github/copilot-instructions.md).
- how to use instruction files to guide Copilot for repetitive or templated tasks.
- the difference between repository-wide instructions and task-specific instructions.

## Scenario

As any good dev shop, Tailspin Toys has a set of guidelines and requirements for development practices. These include:

- API always needs unit tests.
- UI should be in dark mode and have a modern feel.
- documentation should be added to code.

Through the use of instruction files you'll ensure Copilot has the right information to perform the tasks in alignment with the practices highlighted.

> [!IMPORTANT]
> Instruction files are only considered by Copilot Chat at the time of this writing (including ask, edit and agent mode). Code completions are not yet supported. 

## Before you begin

We're going to be making some code changes, so we should follow our usual practice of creating a new branch to work in. This will allow us to make changes without affecting the main branch until we're ready.

1. Return to your codespace from the previous exercise.
2. Open a new terminal window inside your codespace by selecting <kbd>Ctl</kbd>+<kbd>\`</kbd>.
3. Create and switch to a new branch by running the following command in the terminal:

   ```bash
   git checkout -b add-filters
   ```

## Custom instructions

Custom instructions allow you to provide context and preferences to Copilot chat, so that it can better understand your coding style and requirements. This is a powerful feature that can help you steer Copilot to get more relevant suggestions and code snippets. You can specify your preferred coding conventions, libraries, and even the types of comments you like to include in your code.

> [!NOTE]
> Instructions in the `.github/copilot-instructions.md` file are sent with **every** prompt to Copilot chat. As a result, it's best to keep the content focused on guidelines and information relevant to the entire project rather than specific tasks. For specific tasks you can create instruction files, which we'll cover a little later in this exercise.

## Using GitHub Copilot Chat before updating custom instructions

To see the impact of custom instructions, we will start by sending a prompt with the current version of the file. We'll then update the file, send the same prompt again, and note the difference.

1. Open the GitHub codespace if not already open. Feel free to close any open files from the previous exercise.
2. Open **server/routes/games.py**.
3. Open **Copilot chat** 
4. Create a new chat session by selecting the **New Chat** button, which will remove any previous context.

   ![Screenshot of the New Chat button being highlighted in the Copilot Chat panel](images/copilot-new-chat.png)

5. Select **Ask** from the modes dropdown.

   ![Screenshot of the Ask mode being highlighted in the Copilot Chat panel](images/copilot-chat-ask.png)

6. Send the following prompt to create a new endpoint to return all publishers:

   ```plaintext
   Create a new endpoint to return a list of all publishers. It should include the name and id.
   ```

7. Notice the generated code includes [type hints](https://docs.python.org/3/library/typing.html) because the existing code uses them. By default, Copilot uses the current file for context when creating code, and will work to follow the practices it sees in use.
8. Notice the generated code **does not** include a docstring. Copilot is again following the patterns it sees us using, and since docstrings don't already exist it doesn't generate them.

## Adding code requirements and standards to custom instructions 

If we look at the requirements from above, we see we want to include docstrings for functions. Let's update the custom instructions file with this information to ensure the generated suggestions follow our desired practices. We'll then run the same prompt to notice the impact it had on the suggestion.

1. Open **.github/copilot-instructions.md**.
2. Add the following to the bottom of the file to add the requirement for docstrings

   ```markdown
   ## Code guidelines

   - Create docstrings for Python
   - Add JSDoc notes to JavaScript
   ```

3. Close the file, saving if prompted.
4. Open **server/routes/games.py** again to ensure focus for Copilot chat is on our API.
5. Select **New Chat** in Copilot chat to clear the buffer and start a new conversation.

   ![Screenshot of the New Chat button being highlighted in the Copilot Chat panel](images/copilot-new-chat.png)

6. Send the same prompt as before to create the endpoint.

   ```plaintext
   Create a new endpoint to return a list of all publishers. It should include the name and id.
   ```

> [!TIP]
> You can cycle through previous prompts by using the up and down arrows on your keyboard.

7. Notice how the newly generated code includes a docstring inside the function which resembles the following:

   ```python
   """
   Returns a list of all publishers with their id and name.
    
   Returns:
      Response: JSON response containing an array of publisher objects
   """
   ```

8. Also note how the existing code isn't updated, but of course we could ask Copilot to perform that operation if we so desired!
9.  Don't implement the suggested changes, as we will be doing that in the next section. But from this section, you can see how the custom instructions file has provided Copilot with the context it needs to generate code that follows the established guidelines.

## Instruction files for tasks

Coding is often repetitive, with developers performing similar tasks on a regular basis. Copilot is wonderful for allowing you to offload these types of tasks. But these types of tasks, like adding an endpoint, creating a component, or adding a new service pattern implementation often require a particular template or structure to be followed. Instruction files allow you to provide specific requirements for these types of tasks.

We want to create a new endpoint to list all publishers, and to follow the same pattern we used for the existing [games endpoints](../server/routes/games.py), and to create tests which follow the same pattern as the existing [games endpoints tests](../server/tests/test_routes/test_games.py). An instruction file has already been created; let's explore it and see the difference in code it generates.

1. Open **.github/instructions/create-endpoint.instructions.md**.
2. Review the following entries inside the instruction file:

   - An overview of requirements, including that tests must be created, mock objects to be used, and endpoints are created in Flask using blueprints.
   - Links to two existing files which follow the patterns we want - both the games blueprint and tests. Notice how these are setup as normal markdown links, allowing an instruction file to incorporate additional files for context.

3. Open **server/app.py**.
4. Return to Copilot Chat and select **New Chat** to start a new session.
5. Select **Edit** from the mode dropdown, which will allow Copilot to update multiple files.

   ![Screenshot of the Edit mode being highlighted in the Copilot Chat panel](images/copilot-edits.png)

6. Select the **Add Context** button to open the context dialog
7. If prompted to allow the codespace to see text and images copied to the clipboard, press **Allow**.
8. Select **Instructions** from the dropdown at the top of your codespace.

> [!TIP]
> If the list of options is long, you can type **instructions** to filter to the Instructions option then select **Instructions**.

9.  Select **create-endpoint .github/instructions** to add the instruction file to the context.

   ![Screenshot showing the instruction file being added into Copilot Chat](images/copilot-add-instructions-file.png)

10. Send the same prompt as before to generate the desired endpoint:

   ```plaintext
   Create a new endpoint to return a list of all publishers. It should include the name and id.
   ```

11. Copilot generates the files. Notice how it generates updates across multiple files, like **games.py** and **test_games.py**?
12. After reviewing the code, select **Keep** and **Done** in Copilot Chat to accept the changes.
13. Open a terminal window by selecting <kbd>Ctl</kbd>+<kbd>\`</kbd>.
14. Run the tests by running the script with the following command:

   ```sh
   ./scripts/run-server-tests.sh
   ```

15. Ensure all tests pass. Re-prompt Copilot Chat as needed to ensure the code is correct.
16. Once correct, and all tests pass, open the **Source Control** panel on the left of the Codespace and review the changes made by Copilot.
18. Stage the changes by selecting the **+** icon in the **Source Control** panel.
19. Generate a commit message using the **Sparkle** button.

   ![Screenshot of the Source Control panel showing the changes made](images/source-control-changes.png)

20. Commit the changes to your repository by selecting **Commit**.

## Summary

Congratulations! You explored how to ensure Copilot has the right context to generate code following the practices your organization has set forth. This can be done at a repository level with the `.github/copilot-instructions.md` file, or on a task basis with instruction files. You explored:

- how to provide Copilot with project-specific context, coding guidelines and documentation standards using custom instructions.
- how to use instruction files to guide Copilot for repetitive or templated tasks.
- the difference between repository-wide instructions and task-specific instructions.

Next we'll use [agent mode to add functionality to the site](./3-copilot-agent-mode-vscode.md).
