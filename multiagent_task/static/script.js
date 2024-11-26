document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('blogForm').addEventListener('submit', async function (e) {
        e.preventDefault(); // Prevent the default form submission

        const topic = document.getElementById('topic').value;
        const responseDiv = document.getElementById('response');
        responseDiv.innerHTML = "<p>Generating... Please wait.</p>";

        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic: topic }),
            });

            const data = await response.json();

            if (response.ok) {
                responseDiv.innerHTML = `
                    <h2>Outline:</h2>
                    <p>${data.outline}</p>
                    <h2>Content:</h2>
                    <p>${data.content}</p>
                    <h2>Formatted Content:</h2>
                    <p>${data.formatted_content}</p>
                `;
            } else {
                responseDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        } catch (error) {
            responseDiv.innerHTML = `<p>Unexpected error: ${error.message}</p>`;
        }
    });
});
