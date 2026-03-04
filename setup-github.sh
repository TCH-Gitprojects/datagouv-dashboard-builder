#!/bin/bash

# GitHub Repository Setup Script for DataGouv Dashboard Builder
# This script helps you create a GitHub repository and push your code

echo "=========================================="
echo "DataGouv Dashboard Builder - GitHub Setup"
echo "=========================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: Git is not installed. Please install Git first."
    exit 1
fi

# Check if GitHub CLI is installed
if command -v gh &> /dev/null; then
    echo "GitHub CLI (gh) detected! You can use it to create repos."
    USE_GH=true
else
    echo "GitHub CLI not found. You'll need to manually create the repo on GitHub."
    USE_GH=false
fi

echo ""
echo "Step 1: Initialize Git repository"
echo "----------------------------------"
git init
git branch -m main

echo ""
echo "Step 2: Add all files to staging"
echo "----------------------------------"
git add .

echo ""
echo "Step 3: Create initial commit"
echo "----------------------------------"
git commit -m "Initial commit: DataGouv Dashboard Builder"

echo ""
if [ "$USE_GH" = true ]; then
    echo "Step 4: Create GitHub repository using GitHub CLI"
    echo "--------------------------------------------------"
    echo "Choose visibility:"
    echo "  1) Public"
    echo "  2) Private"
    read -p "Enter choice (1 or 2): " choice
    
    if [ "$choice" = "1" ]; then
        gh repo create datagouv-dashboard-builder --public --source=. --push
    else
        gh repo create datagouv-dashboard-builder --private --source=. --push
    fi
else
    echo "Step 4: Manual GitHub repository creation"
    echo "------------------------------------------"
    echo "1. Go to https://github.com/new"
    echo "2. Enter repository name: datagouv-dashboard-builder"
    echo "3. Choose Public or Private"
    echo "4. DO NOT initialize with README (we already have one)"
    echo "5. Click 'Create repository'"
    echo ""
    read -p "Press Enter after creating the repository on GitHub..."
    echo ""
    echo "Step 5: Add remote and push"
    echo "----------------------------"
    read -p "Enter your GitHub username: " username
    git remote add origin "https://github.com/$username/datagouv-dashboard-builder.git"
    git push -u origin main
fi

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "Your repository is now on GitHub!"
echo ""
echo "To run the app locally:"
echo "  1. cd datagouv-dashboard-builder"
echo "  2. npm install"
echo "  3. npm run dev"
echo ""
echo "Open http://localhost:5173 in your browser"
