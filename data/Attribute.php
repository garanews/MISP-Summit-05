// app/Model/Attribute.php

if($a['type'] == 'ssdeep'){
 if(function_exists('ssdeep_fuzzy_compare')){
    $this->FuzzyCorrelateSsdeep = ClassRegistry::init('FuzzyCorrelateSsdeep');
    $fuzzyIds = $this->FuzzyCorrelateSsdeep->query_ssdeep_chunks($a['value'], $a['id']);
    if(!empty($fuzzyIds)){
     $ssdeepIds = $this->find('list', array(
        'recursive' => -1,
        'conditions' => array('Attribute.type' => 'ssdeep', 'Attribute.id' => $fuzzyIds),
        'fields' => array('Attribute.id', 'Attribute.value1')
     ));
     $extraConditions = array('Attribute.id' => array());
     $threshold = !empty(Configure::read('MISP.ssdeep_correlation_threshold'))? 
                  Configure::read('MISP.ssdeep_correlation_threshold'):40;
     foreach($ssdeepIds as $k => $v){
        $ssdeep_value = ssdeep_fuzzy_compare($a['value'], $v);
        if($ssdeep_value >= $threshold){$extraConditions['Attribute.id'][] = $k;}
}}}}