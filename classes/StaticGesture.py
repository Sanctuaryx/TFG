class Hand:
    def __init__(self, roll, pitch, yaw, gyro, accel, finger_flex, calibration):
        self._roll = roll
        self._pitch = pitch
        self._yaw = yaw
        self._finger_flex = finger_flex
        self._gyro = gyro
        self._accel = accel
        self._calibration = calibration
        
    @property
    def roll(self):
        return self._roll
    
    @roll.setter
    def roll(self, roll):
        self._roll = roll
        
    @property
    def pitch(self):
        return self._pitch
    
    @pitch.setter   
    def pitch(self, pitch):
        self._pitch = pitch
        
    @property
    def yaw(self):
        return self._yaw
    
    @yaw.setter
    def yaw(self, yaw):
        self._yaw = yaw
        
    @property
    def finger_flex(self):
        return self._finger_flex
    
    @finger_flex.setter
    def finger_flex(self, finger_flex):
        self._finger_flex = finger_flex
        
    @property
    def gyro(self):
        return self._gyro
    
    @gyro.setter
    def gyro(self, gyro):
        self._gyro = gyro
        
    @property
    def accel(self):
        return self._accel
    
    @accel.setter
    def accel(self, accel):
        self._accel = accel
        
    @property
    def calibration(self):
        return self._calibration
    
    @calibration.setter
    def calibration(self, calibration):
        self._calibration = calibration

class GestureDto:
    def __init__(self, id, name, left_hand : Hand, right_hand : Hand):
        self._id = id
        self._name = name
        self._left_hand = left_hand
        self._right_hand = right_hand
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def left_hand(self):
        return self._left_hand
    
    @left_hand.setter
    def left_hand(self, left_hand):
        self._left_hand = left_hand
    
    @property
    def right_hand(self):
        return self._right_hand
    
    @right_hand.setter  
    def right_hand(self, right_hand):
        self._right_hand = right_hand

    