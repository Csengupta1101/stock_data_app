document.getElementById("stockForm").addEventListener("submit", function (event) {
    event.preventDefault();

    var startDate = document.getElementById("startDate").value;
    var endDate = document.getElementById("endDate").value;
    var companyName = document.getElementById("companyName").value;
    var outputFolder = document.getElementById("outputFolder").value;

    fetch(`/api/fetch_stock_data?start_date=${startDate}&end_date=${endDate}&company_name=${companyName}&output_folder=${outputFolder}`, {
        method: "GET"
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("statusMessage").textContent = data.message;
    })
    .catch(error => {
        console.error("Error:", error);
    });
});
