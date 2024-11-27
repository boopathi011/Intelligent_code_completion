$(document).ready(function() {
    $('#generateBtn').click(function() {
        const codeInput = $('#codeInput').val();

        // Post code to backend
        $.ajax({
            url: 'http://127.0.0.1:5000/generate',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ code: codeInput }),
            success: function(response) {
                // Display generated commented code and documentation
                $('#codeOutput').text(response.commented_code);
                $('#docOutput').text(response.documentation);

                // Show the download button if documentation is generated
                if (response.documentation) {
                    $('#downloadDocBtn').show();
                }
            },
            error: function(error) {
                console.log("Error:", error);
                $('#codeOutput').text("An error occurred while generating comments.");
            }
        });
    });

    // Download documentation as text file
    $('#downloadDocBtn').click(function() {
        const docText = $('#docOutput').text();
        const blob = new Blob([docText], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = 'documentation.txt';
        a.click();
        
        URL.revokeObjectURL(url);
    });
});
