// import java.util.Scanner;
public class Mergesort {
	public static void sort(int array[],int si, int ei){
		 if (si >= ei){
			return;
		}
		int mid = si + (ei - si)/2;
		sort(array, si, mid);
		sort(array, mid+1, ei);
		merge(array,si,mid,ei);
	}
	public static void merge(int arr[],int si, int mid, int ei){
		// System.err.println("arr.length ="+arr.length+"\n"+"ei-si+1 = "+(ei-si+1));
		int temp[] = new int [ei-si+1];
		int i = si;//idx for 1st sort part
		int j = mid+1;//idx for 2nd sorted part
		int k = 0;//idx for temp
		
		while ( i <= mid && j <= ei){
			if (arr[i] < arr[j]){
				temp[k] = arr[i];
				i++;
			} else {
				temp[k] = arr[j];
				j++;
			}
			k++;
		}

		//for leftover elements of 1st sorted part
		while (i <= mid){
			temp[k++] = arr[i++];
		}
		//for leftover elements of 2nd sorted part 
		while (j <= ei){
			temp[k++] = arr[j++];
		}

		//copy temp to original array
		for (k = 0, i = si; k<temp.length; k++,i++){
			arr[i] = temp[k];
		}
		}
	public static void main (String args[]){
		int arr[] = {2,3,6,8,4,3};
		sort(arr,0,(arr.length)-1);
		for(int i = 0 ; i< arr.length; i++){
			System.out.print(arr[i]+" ");
		}
	}
}
