# System Explorer Prototype

This repository contains a proof-of-concept for the **System Exploration & Inventory Builder** project for RUXAILAB GSoC 2026.

## Overview
The goal of this tool is to analyze a website as a complete system rather than isolated pages. It focuses on:
* **Controlled Crawling**: Staying within a defined scope.
* **Mandatory Page Detection**: Automatically identifying Home, Contact, and Accessibility Statement pages.
* **Component Inventory**: Identifying forms and interactive elements for accessibility sampling.

## Setup
1. Install dependencies:
   ```bash
   pip install playwright
   playwright install chromium
   ```
2. Run the explorer:
   ```bash
   python explorer.py
   ```
