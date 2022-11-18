//Not in workable form
public class Revise_merge{
    static void printArr(int inputArray[]){
			for (int i = 0; i < inputArray.length; i++){
					System.out.print(inputArray[i]+" ");
		    }
    }
	public static void main (String args[]){
		int sizeOfInput = 5;//Size to be inputed by user
//		int input_array[] = new int[n];
		int inputArray[] = {3,5,2,1,7};
		Resources ob = new Resources();
		ob.quickSort(inputArray, 0, (inputArray.length - 1));
		//printing final array
		printArr(inputArray);
	}
}
class Resources{
	void quickSort(int arr[], int si, int ei){
		//Base case
	    if (si >= ei){
			return;
		}
		//kaam
		int pIdx = arrangePivot(arr,si,ei);
		quickSort(arr, si, pIdx-1);//Left
		quickSort(arr, pIdx+1, ei);//Right
	}
	int arrangePivot(int arr[],int si, int ei){
		int i = si - 1;
		int pivot = arr[ei];
		for (int j = si; j < ei; j++){
			if (arr[j] < pivot){
				i++;
				int temp = arr[j];
				arr[j] = arr[i];
				arr[i] = temp;
			}
		}
		i++;
		arr[ei] = arr[i];
		arr[i] = pivot;
		
		return i;
   }
}
