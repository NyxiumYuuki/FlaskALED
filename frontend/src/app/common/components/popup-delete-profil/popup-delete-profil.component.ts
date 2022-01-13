import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {MessageService} from "../../services/message/message.service";
import {HttpParams} from "@angular/common/http";



@Component({
  selector: 'app-popup-delete-profil',
  templateUrl: './popup-delete-profil.component.html',
  styleUrls: ['./popup-delete-profil.component.scss']
})
export class PopupDeleteProfilComponent implements OnInit
{
    id: number;
    me: boolean = false; // on se supprime soi-même
    email: string = "";


    constructor( private messageService: MessageService,
                 public dialogRef: MatDialogRef<PopupDeleteProfilComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any ) { }


    ngOnInit(): void {
        this.id = this.data.id;
        this.me = this.data.me;
        this.email = this.data.email;
    }


    // Appuie sur 'valider'
    onValider(): void
    {
        if(this.me)
        {
            this.messageService
                .delete("user/delete")
                .subscribe(ret => this.onValiderCallback(ret), err => this.onValiderCallback(err));
        }
        else {
            let params = new HttpParams();
            params = params.set("id", this.id);
            this.messageService
                .delete("admin/delete", params)
                .subscribe(ret => this.onValiderCallback(ret), err => this.onValiderCallback(err));
        }
    }


    // Callback de onValider
    onValiderCallback(retour: any): void
    {
        if(retour.status === "success")
        {
            this.dialogRef.close(retour);
        }
        else if(retour.status === "error")
        {
            console.log(retour);
            this.dialogRef.close(retour);
        }
        else {
            console.log(retour);
            this.dialogRef.close(null);
        }
    }

}
