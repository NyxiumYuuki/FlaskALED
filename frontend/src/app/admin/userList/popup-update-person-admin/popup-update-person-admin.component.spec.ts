import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PopupUpdatePersonAdminComponent } from './popup-update-person-admin.component';

describe('PopupUpdatePersonAdminComponent', () => {
  let component: PopupUpdatePersonAdminComponent;
  let fixture: ComponentFixture<PopupUpdatePersonAdminComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PopupUpdatePersonAdminComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PopupUpdatePersonAdminComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
