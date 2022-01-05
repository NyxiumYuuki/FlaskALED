import { Component } from '@angular/core';
import {HashageService} from "../../common/services/hashage/hashage.service";
import {Router} from "@angular/router";
import {CheckEmailService} from "../../common/services/checkEmail/check-email.service";
import {MatDialog} from "@angular/material/dialog";
import {PopupConfirmRegisterComponent} from "../popup-confirm-register/popup-confirm-register.component";



@Component({
  selector: 'app-page-register',
  templateUrl: './page-register.component.html',
  styleUrls: ['./page-register.component.scss']
})
export class PageRegisterComponent
{
    person = {
        id: "",
        nickname: "",
        email: "",
        hash_pass: "",
        role: "user"
    };
    password: string = "";
    confirmPassword: string = "";
    hasError: boolean = false;
    errorMessage: string = "";


    constructor( private hashageService: HashageService,
                 private checkEmailService: CheckEmailService,
                 private router: Router,
                 public dialog: MatDialog ) { }


    // Envoie de l'utilisateur au backend
    onValider(): void
    {
        this.checkField();
        if(!this.hasError)
        {
            this.person.hash_pass = this.hashageService.run(this.password);

            // FAUX CODE
            const retour = { status: "succes", data: {} };
            this.onValiderCallback(retour);

            // VRAI CODE
            /*
            this.messageService
                .sendMessage('register', this.user)
                .subscribe(retour => this.onValiderCallback(retour));
            */
        }
    }


    // Callback de "onValider"
    onValiderCallback(retour: any): void
    {
        if(retour.status === "error")
        {
            console.log(retour);
        }
        else
        {
            this.dialog
                .open(PopupConfirmRegisterComponent, {})
                .afterClosed()
                .subscribe(retour => this.router.navigateByUrl("/"));
        }
    }


    // Check les champs saisis par l'utilisateur
    checkField(): void
    {
        if(this.person.nickname.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'pseudo'.";
            this.hasError = true;
        }
        else if(this.person.email.length === 0) {
            this.errorMessage = "Veuillez remplir le champ 'email'.";
            this.hasError = true;
        }
        else if(!this.checkEmailService.isValidEmail(this.person.email)) {
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
