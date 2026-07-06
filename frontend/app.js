fetch("http://localhost:8080/startups")
  .then((response) => response.json())
  .then((data) => {
    const tableBody = document.querySelector("#startupTable tbody");

    data.forEach((startup) => {
      const row = `
                <tr>
                    <td>${startup.id}</td>
                    <td>${startup.company}</td>
                    <td>${startup.country}</td>
                    <td>${startup.sector}</td>
                    <td>${startup.funding}</td>
                </tr>
            `;

      tableBody.innerHTML += row;
    });
  });
