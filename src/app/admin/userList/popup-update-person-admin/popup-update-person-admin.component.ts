import {Component, Inject, OnInit} from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material/dialog";
import {CheckEmailService} from "../../../common/services/checkEmail/check-email.service";
import {MessageService} from "../../../common/services/message/message.service";



@Component({
  selector: 'app-popup-update-person-admin',
  templateUrl: './popup-update-person-admin.component.html',
  styleUrls: ['./popup-update-person-admin.component.scss']
})
export class PopupUpdatePersonAdminComponent implements OnInit
{
    id: number = 0;
    is_admin: boolean = false;
    newPassword: string = "";

    confirmNewPassword: string = "" ;
    changePassword: boolean = false ;
    hasError: boolean = false;
    errorMessage: string = "" ;


    constructor( public dialogRef: MatDialogRef<PopupUpdatePersonAdminComponent>,
                 @Inject(MAT_DIALOG_DATA) public data: any,
                 private checkEmailService: CheckEmailService,
                 private messageService: MessageService ) { }


    ngOnInit(): void
    {
        this.id = this.data.person.id;
        this.is_admin = this.data.person.is_admin;
    }


    // Appuie sur le bouton "valider"
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            let data = {};
            if(this.changePassword) data = { id: this.id, is_admin: this.is_admin, password: this.newPassword }
            else data = { id: this.id, is_admin: this.is_admin };
            this.messageService
                .put("admin/update/user", data)
                .subscribe(ret => this.onValiderCallback(ret), err => this.onValiderCallback(err));
        }
    }


    // Callback de 'onValider'
    onValiderCallback(retour: any)
    {
        if(retour.status !== 'success')
        {
            console.log(retour);
            this.errorMessage = retour.error.message;
            this.hasError = true;
        }
        else
        {
            this.dialogRef.close(this.is_admin);
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if((this.changePassword) && (this.newPassword.length === 0)) {
            this.errorMessage = "Veuillez remplir le champ 'mot de passe'";
            this.hasError = true;
        }
        else if((this.changePassword) && (this.newPassword !== this.confirmNewPassword)) {
            this.errorMessage = "Le mot de passe est différent de sa confirmation";
            this.hasError = true;
        }
        else {
            this.errorMessage = "" ;
            this.hasError = false;
        }
    }

}
