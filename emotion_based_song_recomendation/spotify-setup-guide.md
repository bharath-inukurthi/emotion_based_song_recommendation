# Setting Up a Spotify Developer Application

## Prerequisites
- A Spotify account (free or premium)
- A web browser

## Step 1: Access Spotify Developer Portal
1. Go to [Spotify Developer Portal](https://developer.spotify.com/)
2. Login with your spotify account (If not exists create one)
3. Click on your profile icon in the top-right corner
4. Select "Dashboard" from the dropdown menu


## Step 2: Navigate the Developer Dashboard
1. you'll be taken to the Spotify Developer Dashboard
2. If this is your first time, you might need to agree to the Developer Terms of Service
3. Click the "Create App" button 

## Step 3: Create Your Application
1. In the create app form, fill out:
   - **App name**: Choose a name for your application
   - **App description**: Brief description of what your app will do
   - **Redirect URI**: Enter `http://localhost:8501` (default port for streamlit)
   - **Select required API and SDK**: check box "Web API" and "Web Playback SDK"
   - Check the checkbox agreeing to Terms of Service
2. Click "Create" at the bottom of the form

## Step 4: Get Your Credentials
1. After creation, you'll be taken to your app's dashboard
2. Your **Client ID** will be displayed on this page
3. To view your **Client Secret**:
   - Click "Settings" in the top-right
   - Look for the Client Secret field
   - Click "View Client Secret"

## Step 5: Configure Additional Settings(This step is not always necessary)
1. While in the Settings page:
   - Add additional Redirect URIs if needed
   - Set up any required app settings
   - Configure allowed OAuth scopes
2. Remember to click "Save" after making changes

## Step 6: Secure Your Credentials
- Store your credentials securely:
  ```
  SPOTIFY_CLIENT_ID=your_client_id_here
  SPOTIFY_CLIENT_SECRET=your_client_secret_here
  ```
- Never share or expose these credentials
- Use environment variables in your application

## Security Best Practices
- Keep your Client Secret confidential
- Don't commit credentials to version control
- Reset credentials if they're ever exposed
- Use secure environment variables

## Troubleshooting Common Issues
1. Can't see the Dashboard?
   - Make sure you're logged in
   - Try clearing browser cache
   - Use an incognito/private window

2. Can't create an app?
   - Verify your Spotify account is validated
   - Accept all terms and conditions
   - Check if you have reached the app limit

3. Redirect URI issues?
   - Ensure exact match in your code
   - Include protocol (http:// or https://)
   - No trailing slashes unless specified

## Need Help?
- Visit [Spotify Developer Documentation](https://developer.spotify.com/documentation/)
- Check [Spotify Developer Forums](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer)
- Review [API Guidelines](https://developer.spotify.com/documentation/general/guides/api-guidelines)
