// Create a bar chart that displays the number of pageviews and clicks by day
var ctx = document.getElementById("myChart").getContext("2d");
var chartData = {
  labels: ["Day 1", "Day 2", "Day 3"],
  datasets: [
    {
      label: "Pageviews",
      data: [100, 200, 300],
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
    },
    {
      label: "Clicks",
      data: [50, 100, 150],
      backgroundColor: "rgba(255,159,64,0.4)",
      borderColor: "rgba(255,159,64,1)",
    },
  ],
};
var myChart = new Chart(ctx, {
  type: "bar",
  data: chartData,
  options: {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
  },
});
