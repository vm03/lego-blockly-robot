Blockly.Blocks['motor'] = {
  init: function() {
    this.jsonInit({
      "type": "on_motor",
      "message0": "Вкл %1 мотор на %2 сек %3",
      "args0": [
        {
          "type": "field_dropdown",
          "name": "MOTOR",
           "options": [
              [
                "оба",
                "both"
              ],
              [
                "левый",
                "left"
              ],
              [
                "правый",
                "right"
              ]
          ]
       },
       {
      "type": "field_number",
      "name": "TIMES",
      "value": 1,
      "min": 0,
      "max": 100,
      "precision": 1
       },
        {
          "type": "field_dropdown",
          "name": "DIRECTION",
           "options": [
              [
                "вперед",
                "forward"
              ],
              [
                "назад",
                "backward"
              ]
          ]

       }],
     "inputsInline": true,
     "previousStatement": null,
     "nextStatement": null,
     "colour": 230,
     "tooltip": "",
     "helpUrl": ""
  });
 }
};
Blockly.Blocks['speed'] = {
  init: function() {
    this.jsonInit({
      "type": "motor_speed",
      "message0": "Установить скорость: %1",
      "args0": [{
      "type": "field_number",
      "name": "SPEED",
      "value": 10,
      "min": 0,
      "max": 10,
      "precision": 1
       }],
     "inputsInline": true,
     "previousStatement": null,
     "nextStatement": null,
     "colour": 230,
     "tooltip": "",
     "helpUrl": ""
  });
 }
};
Blockly.Blocks['stop'] = {
  init: function() {
    this.jsonInit({
      "type": "motor_stop",
      "message0": "стоп",
     "inputsInline": true,
     "previousStatement": null,
     "nextStatement": null,
     "colour": 20,
     "tooltip": "",
     "helpUrl": ""
  });
 }
};

Blockly.Python['motor'] = function(block) {
    var motorN = block.getFieldValue('MOTOR');
    var timeN = block.getFieldValue('TIMES');
    var directionN = block.getFieldValue('DIRECTION');
    return 'SetMotor(\'' + motorN + '\', ' + timeN + ', \'' + directionN +'\')\n';
};


Blockly.Python['speed'] = function(block) {
    var speedN = block.getFieldValue('SPEED');
    return 'SetSpeed(' + speedN + ')\n';
};

Blockly.Python['stop'] = function(block) { return 'StopMotor()\n'; };
