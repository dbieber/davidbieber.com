// Create a script tag to load Chart.js from CDN
const chartScript = document.createElement('script');
chartScript.src = 'https://cdn.jsdelivr.net/npm/chart.js';
document.head.appendChild(chartScript);

// Function to create the chart
function createWritingActivityChart() {
  const data = [
    { month: 'Jan 2020', wordCount: 43 },
    { month: 'Feb 2020', wordCount: 0 },
    { month: 'Mar 2020', wordCount: 0 },
    { month: 'Apr 2020', wordCount: 10505 },
    { month: 'May 2020', wordCount: 7154 },
    { month: 'Jun 2020', wordCount: 2738 },
    { month: 'Jul 2020', wordCount: 2929 },
    { month: 'Aug 2020', wordCount: 10397 },
    { month: 'Sep 2020', wordCount: 5920 },
    { month: 'Oct 2020', wordCount: 14910 },
    { month: 'Nov 2020', wordCount: 49682 },
    { month: 'Dec 2020', wordCount: 38889 },
    { month: 'Jan 2021', wordCount: 33513 },
    { month: 'Feb 2021', wordCount: 18108 },
    { month: 'Mar 2021', wordCount: 9834 },
    { month: 'Apr 2021', wordCount: 3234 },
    { month: 'May 2021', wordCount: 484 },
    { month: 'Jun 2021', wordCount: 4002 },
    { month: 'Jul 2021', wordCount: 21917 },
    { month: 'Aug 2021', wordCount: 17173 },
    { month: 'Sep 2021', wordCount: 25292 },
    { month: 'Oct 2021', wordCount: 27411 },
    { month: 'Nov 2021', wordCount: 11853 },
    { month: 'Dec 2021', wordCount: 17109 },
    { month: 'Jan 2022', wordCount: 36472 },
    { month: 'Feb 2022', wordCount: 12645 },
    { month: 'Mar 2022', wordCount: 20724 },
    { month: 'Apr 2022', wordCount: 21027 },
    { month: 'May 2022', wordCount: 9943 },
    { month: 'Jun 2022', wordCount: 1760 },
    { month: 'Jul 2022', wordCount: 9138 },
    { month: 'Aug 2022', wordCount: 5537 },
    { month: 'Sep 2022', wordCount: 8801 },
    { month: 'Oct 2022', wordCount: 8782 },
    { month: 'Nov 2022', wordCount: 2966 },
    { month: 'Dec 2022', wordCount: 9164 },
    { month: 'Jan 2023', wordCount: 51324 },
    { month: 'Feb 2023', wordCount: 33039 },
    { month: 'Mar 2023', wordCount: 27756 },
    { month: 'Apr 2023', wordCount: 23484 },
    { month: 'May 2023', wordCount: 29023 },
    { month: 'Jun 2023', wordCount: 18023 },
    { month: 'Jul 2023', wordCount: 16453 },
    { month: 'Aug 2023', wordCount: 38652 },
    { month: 'Sep 2023', wordCount: 26740 },
    { month: 'Oct 2023', wordCount: 76299 },
    { month: 'Nov 2023', wordCount: 13393 },
    { month: 'Dec 2023', wordCount: 17010 },
    { month: 'Jan 2024', wordCount: 21780 },
    { month: 'Feb 2024', wordCount: 6195 },
    { month: 'Mar 2024', wordCount: 13235 },
    { month: 'Apr 2024', wordCount: 12506 },
    { month: 'May 2024', wordCount: 8308 },
    { month: 'Jun 2024', wordCount: 3564 },
    { month: 'Jul 2024', wordCount: 6196 },
    { month: 'Aug 2024', wordCount: 2469 }
  ];

  const noAIData = [
    { month: 'Dec 2019', wordCount: 3043 },
    { month: 'Jan 2020', wordCount: 43 },
    { month: 'Apr 2020', wordCount: 10505 },
    { month: 'May 2020', wordCount: 7154 },
    { month: 'Jun 2020', wordCount: 2738 },
    { month: 'Jul 2020', wordCount: 2929 },
    { month: 'Aug 2020', wordCount: 10397 },
    { month: 'Sep 2020', wordCount: 5920 },
    { month: 'Oct 2020', wordCount: 14910 },
    { month: 'Nov 2020', wordCount: 49682 },
    { month: 'Dec 2020', wordCount: 38889 },
    { month: 'Jan 2021', wordCount: 33513 },
    { month: 'Feb 2021', wordCount: 18108 },
    { month: 'Mar 2021', wordCount: 9834 },
    { month: 'Apr 2021', wordCount: 3234 },
    { month: 'May 2021', wordCount: 484 },
    { month: 'Jun 2021', wordCount: 4002 },
    { month: 'Jul 2021', wordCount: 21917 },
    { month: 'Aug 2021', wordCount: 17173 },
    { month: 'Sep 2021', wordCount: 25292 },
    { month: 'Oct 2021', wordCount: 27411 },
    { month: 'Nov 2021', wordCount: 11853 },
    { month: 'Dec 2021', wordCount: 17109 },
    { month: 'Jan 2022', wordCount: 36472 },
    { month: 'Feb 2022', wordCount: 12645 },
    { month: 'Mar 2022', wordCount: 20724 },
    { month: 'Apr 2022', wordCount: 21027 },
    { month: 'May 2022', wordCount: 9943 },
    { month: 'Jun 2022', wordCount: 1760 },
    { month: 'Jul 2022', wordCount: 9138 },
    { month: 'Aug 2022', wordCount: 5537 },
    { month: 'Sep 2022', wordCount: 8801 },
    { month: 'Oct 2022', wordCount: 8782 },
    { month: 'Nov 2022', wordCount: 2966 },
    { month: 'Dec 2022', wordCount: 9164 },
    { month: 'Jan 2023', wordCount: 27945 },
    { month: 'Feb 2023', wordCount: 26236 },
    { month: 'Mar 2023', wordCount: 19005 },
    { month: 'Apr 2023', wordCount: 20825 },
    { month: 'May 2023', wordCount: 24546 },
    { month: 'Jun 2023', wordCount: 15705 },
    { month: 'Jul 2023', wordCount: 16163 },
    { month: 'Aug 2023', wordCount: 31600 },
    { month: 'Sep 2023', wordCount: 18133 },
    { month: 'Oct 2023', wordCount: 28150 },
    { month: 'Nov 2023', wordCount: 8848 },
    { month: 'Dec 2023', wordCount: 15074 },
    { month: 'Jan 2024', wordCount: 20407 },
    { month: 'Feb 2024', wordCount: 4538 },
    { month: 'Mar 2024', wordCount: 6325 },
    { month: 'Apr 2024', wordCount: 9881 },
    { month: 'May 2024', wordCount: 6534 },
    { month: 'Jun 2024', wordCount: 3531 },
    { month: 'Jul 2024', wordCount: 5944 },
    { month: 'Aug 2024', wordCount: 2458 },
    { month: 'Sep 2024', wordCount: 9 }
  ];

  const snippetsData = [
    { month: 'Dec 2019', wordCount: 2619 },
    { month: 'Jan 2020', wordCount: 4849 },
    { month: 'Feb 2020', wordCount: 1968 },
    { month: 'Mar 2020', wordCount: 2645 },
    { month: 'Apr 2020', wordCount: 4676 },
    { month: 'May 2020', wordCount: 1218 },
    { month: 'Jun 2020', wordCount: 408 },
    { month: 'Jul 2020', wordCount: 2530 },
    { month: 'Sep 2020', wordCount: 221 },
    { month: 'Oct 2020', wordCount: 2091 },
    { month: 'Nov 2020', wordCount: 1075 },
    { month: 'Dec 2020', wordCount: 5352 },
    { month: 'Jan 2021', wordCount: 13046 },
    { month: 'Feb 2021', wordCount: 4862 },
    { month: 'Mar 2021', wordCount: 2043 },
    { month: 'Apr 2021', wordCount: 7911 },
    { month: 'May 2021', wordCount: 2176 },
    { month: 'Jun 2021', wordCount: 2413 },
    { month: 'Jul 2021', wordCount: 2777 },
    { month: 'Aug 2021', wordCount: 1905 },
    { month: 'Sep 2021', wordCount: 1315 },
    { month: 'Oct 2021', wordCount: 4752 },
    { month: 'Nov 2021', wordCount: 8249 },
    { month: 'Dec 2021', wordCount: 6044 },
    { month: 'Jan 2022', wordCount: 4108 },
    { month: 'Feb 2022', wordCount: 378 },
    { month: 'Mar 2022', wordCount: 1556 },
    { month: 'Apr 2022', wordCount: 0 },
    { month: 'May 2022', wordCount: 388 },
    { month: 'Jun 2022', wordCount: 1053 },
    { month: 'Jul 2022', wordCount: 3670 },
    { month: 'Sep 2022', wordCount: 1185 },
    { month: 'Oct 2022', wordCount: 336 },
    { month: 'Nov 2022', wordCount: 0 },
    { month: 'Dec 2022', wordCount: 4733 },
    { month: 'Jan 2023', wordCount: 10922 },
    { month: 'Feb 2023', wordCount: 504 },
    { month: 'Mar 2023', wordCount: 3016 },
    { month: 'Apr 2023', wordCount: 0 },
    { month: 'May 2023', wordCount: 0 },
    { month: 'Jun 2023', wordCount: 0 },
    { month: 'Jul 2023', wordCount: 1658 },
    { month: 'Aug 2023', wordCount: 0 },
    { month: 'Sep 2023', wordCount: 1339 },
    { month: 'Oct 2023', wordCount: 0 },
    { month: 'Nov 2023', wordCount: 0 },
    { month: 'Dec 2023', wordCount: 2790 },
    { month: 'Jan 2024', wordCount: 734 },
    { month: 'Feb 2024', wordCount: 0 },
    { month: 'Mar 2024', wordCount: 3760 },
    { month: 'Apr 2024', wordCount: 0 },
    { month: 'May 2024', wordCount: 1713 },
    { month: 'Jun 2024', wordCount: 337 }
  ];

  // Create canvas element
  const canvas = document.createElement('canvas');
  canvas.id = 'writingActivityChart';

  // Create container
  const container = document.createElement('div');
  container.style.maxWidth = '800px';
  container.style.margin = '0 auto';
  container.style.padding = '20px';
  container.appendChild(canvas);

  // Add container to the page
  document.getElementById('writing-activity-chart').appendChild(container);

  // Create no-AI canvas element
  const canvas2 = document.createElement('canvas');
  canvas2.id = 'writingActivityChart-noAI';

  // Create container
  const container2 = document.createElement('div');
  container2.style.maxWidth = '800px';
  container2.style.margin = '0 auto';
  container2.style.padding = '20px';
  container2.appendChild(canvas2);

  // Add container to the page
  document.getElementById('writing-activity-chart-no-ai').appendChild(container2);


  // Create snippets canvas element
  const canvas3 = document.createElement('canvas');
  canvas3.id = 'writingActivityChart-snippets';

  // Create container
  const container3 = document.createElement('div');
  container3.style.maxWidth = '800px';
  container3.style.margin = '0 auto';
  container3.style.padding = '20px';
  container3.appendChild(canvas3);

  // Add container to the page
  document.getElementById('writing-activity-chart-snippets').appendChild(container3);

  function createChart(canvasId, chartData, chartTitle) {
    const canvas = document.getElementById(canvasId);
    const title = document.createElement('h2');
    title.textContent = chartTitle;
    title.style.fontFamily = 'Arial, sans-serif';
    title.style.fontSize = '24px';
    title.style.fontWeight = 'normal';
    title.style.marginBottom = '20px';
    
    canvas.parentNode.insertBefore(title, canvas);

    new Chart(canvas, {
      type: 'bar',
      data: {
        labels: chartData.map(d => d.month),
        datasets: [{
          label: 'Word Count',
          data: chartData.map(d => d.wordCount),
          backgroundColor: '#4A90E2',
          borderRadius: 4,
        }]
      },
      options: {
        responsive: true,
        scales: {
          y: {
            beginAtZero: true,
            grid: {
              drawBorder: false,
            },
            ticks: {
              color: '#333',
            },
            title: {
              display: true,
              text: 'Words',
              color: '#333',
              font: {
                size: 14,
                weight: 'normal'
              }
            }
          },
          x: {
            grid: {
              display: false,
              drawBorder: false,
            },
            ticks: {
              color: '#333',
              maxRotation: 45,
              minRotation: 45
            }
          }
        },
        plugins: {
          legend: {
            display: false
          },
          tooltip: {
            backgroundColor: '#fff',
            titleColor: '#333',
            bodyColor: '#333',
            borderColor: '#ddd',
            borderWidth: 1,
            cornerRadius: 4,
            padding: 10,
          }
        }
      }
    });
  }

  // Function to initialize both charts
  function initializeCharts() {
    createChart('writingActivityChart', data, 'Roam Research Writing by Month');
    createChart('writingActivityChart-noAI', noAIData, 'Roam Research Writing by Month (No AI)');
    createChart('writingActivityChart-snippets', snippetsData, 'Snippets Writing by Month');
  }

  // Create the chart
  chartScript.onload = initializeCharts;
}

// Call the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', createWritingActivityChart);
