import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";



@Component({
  selector: 'app-popup-delete-profil',
  templateUrl: './popup-delete-profil.component.html',
  styleUrls: ['./popup-delete-profil.component.scss']
})
export class PopupDeleteProfilComponent implements OnInit
{
    me: boolean = false; // on se supprime soi-même
    email: string = "";

    constructor( public dialogRef: MatDialogRef<PopupDeleteProfilComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any ) { }

    ngOnInit(): void {
        this.me = this.data.me;
        this.email = this.data.email;
    }

    onValider(): void {
        this.dialogRef.close(true);
    }

}
