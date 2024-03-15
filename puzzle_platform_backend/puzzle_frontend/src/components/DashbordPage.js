import React, { useEffect, useRef, useState } from 'react';
// import Chart from 'chart.js/auto';
import SubscriptionPage from './SubscriptionPage'; 
import LineChart from "./Linechart";
const DashboardPage = () => {
  // const [chartInstance, setChartInstance] = useState(null);
  // const chartRef = useRef(null);
  // const initialized = useRef(false);

  // useEffect(() => {
  //   if (!initialized.current) {
  //     const ctx = chartRef.current.getContext('2d');

  //     const newChartInstance = new Chart(ctx, {
  //       type: 'pie',
  //       data: {
  //         labels: ['Completed', 'Incomplete', 'Skipped'],
  //         datasets: [{
  //           label: 'Task Stats',
  //           data: [10, 5, 3], // Assuming these are the counts of completed, incomplete, and skipped tasks
  //           backgroundColor: [
  //             'rgba(75, 192, 192, 0.2)', // Completed
  //             'rgba(255, 99, 132, 0.2)', // Incomplete
  //             'rgba(255, 206, 86, 0.2)'  // Skipped
  //           ],
  //           borderColor: [
  //             'rgba(75, 192, 192, 1)',   // Completed
  //             'rgba(255, 99, 132, 1)',   // Incomplete
  //             'rgba(255, 206, 86, 1)'    // Skipped
  //           ],
  //           borderWidth: 1
  //         }]
  //       },
  //       options: {
  //         responsive: true,
  //         maintainAspectRatio: false
  //       }
  //     });

  //     setChartInstance(newChartInstance);
  //     initialized.current = true;
  //   } else if (chartInstance) {
  //     // Update chart data
  //     chartInstance.data.datasets[0].data = [10, 5, 3]; // Update with actual data
  //     chartInstance.update();
  //   }

  //   return () => {
  //     if (chartInstance) {
  //       chartInstance.destroy();
  //     }
  //   };
  // }, [chartInstance]);

  return (
    <div className="dashboard-page">
      <LineChart />
    </div>
  );
};

export default DashboardPage;
