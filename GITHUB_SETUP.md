# GitHub Push Setup Guide

## Option 1: Using Personal Access Token (PAT) - Recommended for Quick Setup

### Step 1: Create a Personal Access Token
1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. Give it a name: `Rituva Development`
4. Set expiration (or choose "No expiration" if you prefer)
5. **Select scopes**: Check the `repo` checkbox (this gives full control of private repositories)
6. Click **"Generate token"** at the bottom
7. **IMPORTANT**: Copy the token immediately - you won't be able to see it again!

### Step 2: Use the Token to Push
When you push, use your token as the password:
- Username: Your GitHub username (7717CMI)
- Password: Paste your Personal Access Token (not your GitHub password)

### Step 3: Push Your Code
```powershell
git push -u origin main
```

---

## Option 2: Using SSH Keys (More Secure, One-Time Setup)

### Step 1: Generate SSH Key
```powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter to accept default location, then set a passphrase (optional but recommended).

### Step 2: Copy Your Public Key
```powershell
cat ~/.ssh/id_ed25519.pub
```
Copy the entire output.

### Step 3: Add SSH Key to GitHub
1. Go to: https://github.com/settings/keys
2. Click **"New SSH key"**
3. Give it a title: `Rituva Development`
4. Paste your public key
5. Click **"Add SSH key"**

### Step 4: Update Remote URL
```powershell
git remote set-url origin git@github.com:7717CMI/product_development.git
```

### Step 5: Push Your Code
```powershell
git push -u origin main
```

---

## Current Repository Status
- Remote URL: `https://github.com/7717CMI/product_development.git`
- Branch: `main`
- Latest commit: `c98f1df`

## Troubleshooting 403 Error
The 403 error occurs because:
- GitHub no longer accepts passwords for HTTPS authentication
- You need either a Personal Access Token (Option 1) or SSH keys (Option 2)



