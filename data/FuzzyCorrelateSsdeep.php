// app/Model/FuzzyCorrelateSsdeep.php

public function query_ssdeep_chunks($hash, $attribute_id){
  $chunks = $this->ssdeep_prepare($hash);
  $result = $this->find('list', array(
    'conditions' => array(
      'AND' => array(
        'OR' => array('FuzzyCorrelateSsdeep.chunk_size' => $chunks[0], 'FuzzyCorrelateSsdeep.chunk_size' => $chunks[0] * 2,),
        'OR' => array('FuzzyCorrelateSsdeep.chunk' => $chunks[1], 'FuzzyCorrelateSsdeep.chunk' => $chunks[2])
    )),
    'fields' => array('FuzzyCorrelateSsdeep.attribute_id', 'FuzzyCorrelateSsdeep.attribute_id')
  ));
  $to_save = array();
  foreach (array(1, 2) as $type) {
    foreach ($chunks[$type] as $chunk) {
      $to_save[] = array('attribute_id' => $attribute_id, 'chunk' => $chunk);
  }}
  $this->saveAll($to_save);
  return $result;
}
