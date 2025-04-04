let dummyData = [];

fetch('data/dummyFiles.json')
  .then(res => res.json())
  .then(data => {
    dummyData = data;
  });

function simulateScan() {
  const fs = document.getElementById('fsSelect').value;
  const type = document.getElementById('fileType').value;

  const filtered = dummyData.filter(file =>
    (file.fileSystem === fs) &&
    (type === "all" || file.type === type)
  );

  const tbody = document.querySelector('#resultsTable tbody');
  tbody.innerHTML = "";

  filtered.forEach(file => {
    const row = `
      <tr>
        <td>${file.name}</td>
        <td>${file.type}</td>
        <td>${file.size}</td>
        <td>${file.created}</td>
        <td>${file.deleted}</td>
        <td>${file.status}</td>
      </tr>
    `;
    tbody.innerHTML += row;
  });
}

function exportReport() {
  const rows = Array.from(document.querySelectorAll("tbody tr")).map(row => {
    return Array.from(row.children).map(cell => `"${cell.textContent}"`).join(",");
  });

  const csvContent = "File Name,Type,Size,Created,Deleted,Status\n" + rows.join("\n");
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  const link = document.createElement("a");
  link.setAttribute("href", URL.createObjectURL(blob));
  link.setAttribute("download", "recovery_report.csv");
  link.click();
}
