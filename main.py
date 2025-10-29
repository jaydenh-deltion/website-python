from website import create_app

app = create_app()

if __name__ == '__main__': # Check if the script is run directly
    app.run(debug=True) # Run the Flask app in debug mode