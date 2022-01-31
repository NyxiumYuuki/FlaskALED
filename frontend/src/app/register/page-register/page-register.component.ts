import { Component } from '@angular/core';
import {HashageService} from "../../common/services/hashage/hashage.service";
import {Router} from "@angular/router";
import {CheckEmailService} from "../../common/services/checkEmail/check-email.service";
import {MatDialog} from "@angular/material/dialog";
import {PopupConfirmRegisterComponent} from "../popup-confirm-register/popup-confirm-register.component";
import {MessageService} from "../../common/services/message/message.service";



@Component({
  selector: 'app-page-register',
  templateUrl: './page-register.component.html',
  styleUrls: ['./page-register.component.scss']
})
export class PageRegisterComponent
{
    email: string = "";
    nickname: string = "";
    password: string = "";
    confirmPassword: string = "";
    hasError: boolean = false;
    errorMessage: string = "";


    constructor( private checkEmailService: CheckEmailService,
                 private messageService: MessageService,
                 private router: Router,
                 public dialog: MatDialog ) { }


    // Envoie de l'utilisateur au backend
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            const data = {
                email: this.email,
                nickname: this.nickname,
                password: this.password,
                is_admin: false
            };
            this.messageService
                .post('register', data)
                .subscribe( retour => this.onValiderCallback(retour), err => this.onValiderCallback(err));
        }
    }


    // Callback de "onValider"
    onValiderCallback(retour: any): void
    {
        if(retour.status !== "success")
        {
            console.log(retour);
            this.errorMessage = retour.error.message;
            this.hasError = true;
        }
        else {
            this.dialog
                .open(PopupConfirmRegisterComponent, {})
                .afterClosed()
                .subscribe(retour => this.router.navigateByUrl("/login"));
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.nickname.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'pseudo'.";
            this.hasError = true;
        }
        else if(this.email.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'email'.";
            this.hasError = true;
        }
        else if(!this.checkEmailService.isValidEmail(this.email)) {
            this.errorMessage = "Email invalide.";
            this.hasError = true;
        }
        else if(this.password.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'mot de passe'.";
            this.hasError = true;
        }
        else if(this.password !== this.confirmPassword) {
            this.errorMessage = "Le mot de passe est différent de sa confirmation.";
            this.hasError = true;
        }
        else {
            this.errorMessage = "" ;
            this.hasError = false;
        }
    }

}
