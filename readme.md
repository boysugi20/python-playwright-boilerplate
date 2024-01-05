# Python Playwright Boilerplate

A lightweight and versatile Python Playwright boilerplate designed with privacy and simplicity in mind.

## Table of Contents

-   [Introduction](#introduction)
-   [Installation](#installation)

## Introduction

This boilerplate simplifies the process of setting up a Python Playwright environment for browser automation. It includes basic configurations and integrates a proxy solution for enhanced privacy during automated tasks.

The provided steps guide users through the installation of necessary dependencies using `pipenv`, Playwright setup, and configuring a proxy within the `main.py` script. This allows users to seamlessly integrate their own functionality while maintaining anonymity, making it ideal for a range of automated web interactions.

Feel free to adapt and expand upon this boilerplate to suit your specific automation needs.

## Installation

1. Install pipenv

    ```bash
    pip install pipenv
    ```

2. Install dependencies

    ```bash
    pipenv install
    ```

3. Install Playwright

    ```bash
    playwright install
    ```

4. Configure proxy in `main.py`

    ```python
    PROXY = {"server": "http://myproxy.com:3128", "username": "usr", "password": "pwd"}
    ```

5. Run script

    ```bash
    python main.py
    ```
