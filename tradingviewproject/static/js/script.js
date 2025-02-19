document.addEventListener("DOMContentLoaded", function () {
    let chart; // Variable to store the TradingView chart instance

    // Initialize the chart
    function initializeChart(symbol, timeframe) {
        if (chart) {
            chart.remove(); // Remove existing chart if it exists
        }

        // Create a new TradingView chart
        chart = new TradingView.widget({
            container_id: "chart",
            symbol: symbol === "NIFTY" ? "NSE:NIFTY" : "BSE:SENSEX",
            interval: "5",
            timezone: "Asia/Kolkata",
            theme: "light",
            style: "1",
            locale: "in",
            toolbar_bg: "#f1f3f6",
            enable_publishing: false,
            allow_symbol_change: false,
            details: true,
            hotlist: true,
            calendar: true,
            studies: ["RSI@tv-basicstudies"],
        });

        // Fetch data from the backend
        fetchData(symbol, timeframe);
    }

    // Fetch data from the backend
    function fetchData(symbol, timeframe) {
        fetch(`/get_data?symbol=${symbol}&timeframe=${timeframe}`)
            .then((response) => response.json())
            .then((data) => {
                console.log("Fetched Data:", data);
                // You can use this data to update the chart if needed
            })
            .catch((error) => console.error("Error fetching data:", error));
    }

    // Event listener for the "Update Chart" button
    document.getElementById("update-chart").addEventListener("click", function () {
        const symbol = document.getElementById("symbol").value;
        const timeframe = document.getElementById("timeframe").value;
        initializeChart(symbol, timeframe);
    });

    // Initialize the chart with default values
    initializeChart("NIFTY", "1d");
});