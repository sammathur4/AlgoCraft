class Solution {

    /**
     * @param String $blocks
     * @param Integer $k
     * @return Integer
     */
    function minimumRecolors($blocks, $k) {
         $n = strlen($blocks);
    
    // Count the number of 'W' in the first window of size k
    $current_w_count = 0;
    for ($i = 0; $i < $k; $i++) {
        if ($blocks[$i] == 'W') {
            $current_w_count++;
        }
    }

    $min_operations = $current_w_count;

    // Slide the window across the string
    for ($i = 1; $i <= $n - $k; $i++) {
        // Remove the contribution of the leftmost block going out of the window
        if ($blocks[$i - 1] == 'W') {
            $current_w_count--;
        }
        // Add the contribution of the new block coming into the window
        if ($blocks[$i + $k - 1] == 'W') {
            $current_w_count++;
        }

        // Update the minimum operations required
        $min_operations = min($min_operations, $current_w_count);
    }

    return $min_operations;
    }
}