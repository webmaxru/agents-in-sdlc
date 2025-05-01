# Exercise 0: Prerequisites

Before starting the lab, please ensure you have completed the following setup steps.

## Setting up the Lab Repository

1. Navigate to the [GitHub Repository for this lab](https://github.com/github-samples/agents-in-sdlc).
2. Create your own copy of the repository by selecting the **Use this template** button on the lab repository page. Then select **Create a new repository**.

    ![Use this template button](images/use-template.png)

3. For labs at Microsoft build, please choose **Microsoft-Build-2025** as the GitHub organization. Set the repository name to something you'll remember for the rest of the lab, but be aware that name is visible to all other users also using the GitHub org.

    ![Input the repository template settings](images/repository-template-settings.png)

> [!NOTE]
> This will create a new repository with the same files and structure as the original lab repository.

We will be using this newly created repository to complete the lab exercises.

## Creating a GitHub Codespace

Next up, we will be using a GitHub Codespace to complete the lab exercises. [GitHub Codespaces](https://github.com/features/codespaces) are a cloud-based development environment that allows you to write, run, and debug code directly in your browser. It provides a fully-featured IDE with support for multiple programming languages, extensions, and tools.

1. Navigate to your newly created repository.
2. Select the green **Code** button.

    ![Select the Code button](images/code-button.png)

3. Select the **Codespaces** tab and select the **+** button to create a new Codespace.

    ![Create a new Codespace](images/create-codespace.png)

4. Wait for the Codespace to be created. This may take a few minutes depending on the container image size, the number of extensions being installed and any post install scripts that are being run. Please be patient while the Codespace is being created.

    ![Screenshot showing the Codespace when ready](images/codespace-startup.png)

## Setup Complete

Congratulations, you have created a copy of the lab repository! Now, let's move on to the [next step](./1-mcp.md), utilizing Model Context Protocol (MCP) to provide GitHub Copilot Agent Mode access to a suite of tools.
