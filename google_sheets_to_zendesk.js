function syncToZendesk() {
  // Get the active sheet from the current spreadsheet
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

  // Retrieve all data from the sheet as a 2D array
  const rows = sheet.getDataRange().getValues();

  // Zendesk API endpoint for custom objects
  const zendeskUrl = 'https://your_subdomain.zendesk.com/api/v2/custom_objects/records';

  // Zendesk API authentication details
  const apiToken = 'your_zendesk_api_token'; // Replace with your actual API token
  const userEmail = 'your_email@domain.com'; // Replace with your Zendesk email

  // Loop through each row starting from the second row (skipping headers)
  for (let i = 1; i < rows.length; i++) {
    // Create the payload for the Zendesk API request
    const payload = {
      data: {
        type: 'inventory', // Define the custom object type
        attributes: {
          name: rows[i][0],            // Column 1: Name
          computer_type: rows[i][1],  // Column 2: Computer Type
          serial_number: rows[i][2],  // Column 3: Serial Number
          purchase_date: rows[i][3],  // Column 4: Purchase Date
          device_status: rows[i][4],  // Column 5: Device Status
          assigned_user: rows[i][5]   // Column 6: Assigned User
        }
      }
    };

    // Options for the HTTP POST request
    const options = {
      method: 'post',                    // HTTP method
      contentType: 'application/json',   // Content type of the request
      headers: {
        // Basic Auth header (email/token:apiToken)
        Authorization: 'Basic ' + Utilities.base64Encode(userEmail + '/token:' + apiToken)
      },
      payload: JSON.stringify(payload)   // Convert payload to JSON format
    };

    // Send the POST request to Zendesk API
    UrlFetchApp.fetch(zendeskUrl, options);
  }
}
