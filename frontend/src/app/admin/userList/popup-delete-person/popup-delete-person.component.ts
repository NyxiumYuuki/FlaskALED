import {Component, Inject} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";



@Component({
  selector: 'app-popup-delete-person',
  templateUrl: './popup-delete-person.component.html',
  styleUrls: ['./popup-delete-person.component.scss']
})
export class PopupDeletePersonComponent
{

    constructor( public dialogRef: MatDialogRef<PopupDeletePersonComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any ) { }

}
