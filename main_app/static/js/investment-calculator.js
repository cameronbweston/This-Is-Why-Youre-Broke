// Cached element references
const simpleOutput1 = document.getElementById("siOutput-01")
const simpleOutput2 = document.getElementById("siOutput-02")
const compoundOutput1 = document.getElementById("ciOutput-01")
const compoundOutput2 = document.getElementById("ciOutput-02")
// 

//Add Event Listeners


//

var principal = 0;
var interestRate = 0;
var timesCompounded = 0;
var termOfLoan = 0;
var amount = 0;
let simpleInterestByYear = []
let compoundInterestByYear = []
let yearsForChart = 0;

function simpleInterest() {
  var principal = parseFloat(document.getElementById("principalSimple").value);
  var interestRate = parseFloat(document.getElementById("interestSimple").value);
  interestRate = interestRate / 100;
  var termOfLoan = parseFloat(document.getElementById("termSimple").value);
  var simpleInt = principal * interestRate * termOfLoan;
  var amount = (principal + simpleInt).toFixed(2);
  // get interest each year
  for(let i=0; i <= termOfLoan; i++) {
    let yearlyInvestment = (principal * (1 + (i * interestRate))).toFixed(2)
    simpleInterestByYear.push(yearlyInvestment)
  }
  //
  document.getElementById("siOutput-01").innerHTML = "Interest: $" + simpleInt.toFixed(2);
  document.getElementById("siOutput-02").innerHTML = "Total plus interest: $" + amount;
  document.getElementById("totalInvestmentHeader").innerHTML = `Total investment over the course of ${termOfLoan} years: $${amount}`
}

function compoundInterest() {
  event.preventDefault();
  var principal = parseFloat(document.getElementById("principalCompound").value);
  var interestRate = parseFloat(document.getElementById("interestCompound").value);
  interestRate = interestRate / 100;
  var timesCompounded = parseFloat(document.getElementById("timesCompounded").value);
  var termOfLoan = parseFloat(document.getElementById("termCompound").value);
  var a = interestRate / timesCompounded;
  var b = 1 + a;
  var c = timesCompounded * termOfLoan;
  var d = Math.pow(b, c);
  var amount = (principal * d).toFixed(2);
  document.getElementById("ciOutput-01").innerHTML = "Interest: $" + (amount - principal).toFixed(2);
  document.getElementById("ciOutput-02").innerHTML = "Total plus interest: $" + amount;
}

function changeGraph() {
  //Create the initial chart
  var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: ['2021', '2022', '2023', '2024', '2025', '2026'],
          datasets: [{
              label: 'Investment Over Time',
              backgroundColor: 'rgb(0,214,75, 0.2)',
              data: [],
              fill: true,
              borderColor: 'rgb(0,214,75)',
              tension: 0.1,
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true,
              }
          }
      }
  });

  const buttonSimple = document.getElementById("btnSimple")
  const term = document.getElementById("termSimple")
  //buttonSimple.addEventListener('click', changeGraph())


    simpleInterest()

    console.log(myChart.config.data.labels)
    let yearLabels = []
    let currentYear = parseInt(new Date().getFullYear())
    for (let i=0; i <= term.value; i++) {
      yearLabels.push(currentYear)
      currentYear++
    }
    myChart.data.datasets[0].data = simpleInterestByYear
    myChart.config.data.labels = yearLabels
    myChart.update()
  
}