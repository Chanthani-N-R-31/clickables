<?php
/**
 * Simple form submission handler for REGISTRATION.html
 * In a real application, this would connect to a database.
 */

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get all POST data
    $data = $_POST;
    
    // Log data or save to DB here
    // file_put_contents('submissions.log', json_encode($data) . PHP_EOL, FILE_APPEND);

    // Mock response
    echo json_encode([
        'status' => 'success',
        'message' => 'Registration data received successfully',
        'received_data' => $data
    ]);
} else {
    http_response_code(405);
    echo json_encode([
        'status' => 'error',
        'message' => 'Method not allowed'
    ]);
}
?>
