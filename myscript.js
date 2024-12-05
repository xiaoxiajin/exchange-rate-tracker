
const form = document.getElementById('rateForm');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;

    if (startDate > endDate) {
        resultDiv.textContent = "Error: Start date must be before end date.";
        return;
    }

    try {
        const response = await fetch('http://localhost:5000/rates', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ start_date: startDate, end_date: endDate })
        });

        const data = await response.json();
        if (data.error) {
            resultDiv.textContent = data.error;
            resultDiv.style.display = 'block';
            resultDiv.style.backgroundColor = 'red';
            resultDiv.style.color = 'white';
            resultDiv.style.border = 'none';
        } else {
            resultDiv.innerHTML = `
                <p><strong>Min Rate:</strong> ${data.min_rate.rate.toFixed(4)} CNY per EUR (Date: ${data.min_rate.date})</p>
                <p><strong>Max Rate:</strong> ${data.max_rate.rate.toFixed(4)} CNY per EUR (Date: ${data.max_rate.date})</p>
            `;
            resultDiv.style.display = 'block';
            resultDiv.style.backgroundColor= '#d4edda';
            resultDiv.style.color = 'black';
            resultDiv.style.border ='2px solid #28a745';
            resultDiv.innerHTML += 'Please note that sample data is from 2024-01-01 to 2024-03-04';
        }
    } catch (error) {
        resultDiv.textContent = "Error fetching data. Please try again later.";
        resultDiv.style.display = 'block';
    }
});