public class ParkingSystem {

    private int[] spaces;
    public ParkingSystem(int big, int medium, int small) {
        spaces = new int[4];
        spaces[1] = big;
        spaces[2] = medium;
        spaces[3] = small;
    }
    
    public bool AddCar(int carType) {
        if (spaces[carType] >= 1) {
            spaces[carType]--;
            return true;
        }

        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */