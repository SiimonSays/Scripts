function syncToZendesk() {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const rows = sheet.getDataRange().getValues();
    
    const zendeskUrl = 'https://your_subdomain.zendesk.com/api/v2/custom_objects/records';
    const apiToken = 'your_zendesk_api_token';
    const userEmail = 'your_email@domain.com';
  
    for (let i = 1; i < rows.length; i++) {
      const payload = {
        data: {
          type: 'inventory',
          attributes: {
            name: rows[i][0],
            computer_type: rows[i][1],
            serial_number: rows[i][2],
            purchase_date: rows[i][3],
            device_status: rows[i][4],
            assigned_user: rows[i][5]
          }
        }
      };
  
      const options = {
        method: 'post',
        contentType: 'application/json',
        headers: {
          Authorization: 'Basic ' + Utilities.base64Encode(userEmail + '/token:' + apiToken)
        },
        payload: JSON.stringify(payload)
      };
  
      UrlFetchApp.fetch(zendeskUrl, options);
    }
  }