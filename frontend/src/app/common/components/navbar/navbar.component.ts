import {Component, Input, OnInit} from '@angular/core';
import {ProfilService} from "../../services/profil/profil.service";
import {MessageService} from "../../services/message/message.service";

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.scss']
})
export class NavbarComponent implements OnInit
{
    @Input() pour = "login";

    constructor(private profilService: ProfilService, private messageService: MessageService) { }

    ngOnInit(): void {}

    onDeconnexion(): void
    {
        this.messageService
            .delete('logout')
            .subscribe(retour => this.onDeconnexionCallback(retour), err => this.onDeconnexionCallback(err));
        this.profilService.setId(-1);
        this.profilService.setIsAdmin(false);
    }

    onDeconnexionCallback(retour: any): void
    {
        if(retour.status !== "success") console.log(retour);
    }

}
