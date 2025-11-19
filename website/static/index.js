function deleteNote(noteId) { // Function to delete a note by its ID
    fetch('/delete-note', { // Adjust the URL as needed
        method: 'POST', // Use POST method for deletion
        body: JSON.stringify({ noteId: noteId }) // Send the note ID in the request body
    }).then((_res) => { // Handle the response
        window.location.href = "/";  // Refresh the page after deletion
    })
}