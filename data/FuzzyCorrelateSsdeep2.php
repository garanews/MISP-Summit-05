// app/Model/FuzzyCorrelateSsdeep.php

public function get_all_7_char_chunks($hash){
  $result = '';
  $results = array();
  for ($i = 0; $i < strlen($hash) - 6; $i++) {
    $current = substr($hash, $i, 7);
    $temp = $current . '=';
    $temp = base64_decode($temp);
    $temp = $temp . "\x00\x00\x00";
    $temp = base64_encode($temp);
    if (!in_array($temp, $results)) {
      $results[] = $temp;
    }
  }
  return $results;
}