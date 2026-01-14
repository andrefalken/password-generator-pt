/* Password Generator Class - Main Aplication */
class PasswordGenerator {
    constructor() {
        console.log('🔧 Initializing PasswordGenerator...');
        this.initializeElements();
        this.initEvents();
    }

/* Element Initialization - Finding HTML Elements */
    initializeElements() {
        this.generateBtn = document.getElementById('generateBtn');
        this.quantityInput = document.getElementById('quantity');
        this.passwordOutput = document.getElementById('passwordOutput');
        this.passwordLength = document.getElementById('passwordLength');
        this.generationTime = document.getElementById('generationTime');
        this.copyBtn = document.getElementById('copyBtn');

        if (!this.generateBtn || !this.quantityInput || !this.passwordOutput) {
            console.error('❌ Essential elements not found!');
            this.showError('Erro: Elementos da página não carregaram corretamente.');
            return;
        }

        console.log('✅ All essential elements loaded!');
    }

    /* Event Listeners - User Interaction Handling */
    initEvents() {
        this.generateBtn.addEventListener('click', () => this.generatePassword());

        if (this.copyBtn) {
            this.copyBtn.addEventListener('click', () => this.copyPassword());
        }

        this.quantityInput.addEventListener('change', () => this.updateLengthDisplay());

        this.quantityInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.generatePassword();
        });

        this.updateLengthDisplay();
    }

    /* Password Generation - Main Functionality */
    async generatePassword() {
        console.log('🎯 Generating password...');

        const quantity = parseInt(this.quantityInput.value);

        if (isNaN(quantity) || quantity < 8 || quantity > 50) {
            this.showError('Por favor digite um número entre 8 e 50');
            return;
        }

        this.setLoading(true);
        const startTime = performance.now();

        try {
            console.log('📤 Sending request to server...');

            const response = await fetch('/generate_password', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `quantity=${quantity}`
            });

            console.log('📥 Response received:', response.status);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log('📊 Data received:', data);

            if (data.error) {
                throw new Error(data.error);
            }

            this.passwordOutput.value = data.password;

            if (this.passwordLength) {
                this.passwordLength.textContent = `${data.length} caracteres`;
            }

            if (this.generationTime) {
                const endTime = performance.now();
                this.generationTime.textContent = `Gerado em ${(endTime - startTime).toFixed(0)}ms`;
            }

            this.updateStrengthIndicator(data.password);

            console.log('✅ Password generated successfully!');

        } catch (error) {
            console.error('❌ Error generating password:', error);
            this.showError('Erro gerando senha: ' + error.message);
        } finally {
            this.setLoading(false);
        }
    }

    /* Password Strength Analysis */
    checkPasswordStrength(password) {
        console.log('🔒 Checking password strength...');

        let score = 0;
        const criteria = {
            hasUpperCase: false,
            hasLowerCase: false,
            hasNumbers: false,
            hasSpecialChar: false,
            isLongEnough: false,
            hasGoodLength: false
        };

        criteria.hasUpperCase = /[A-Z]/.test(password);
        criteria.hasLowerCase = /[a-z]/.test(password);
        criteria.hasNumbers = /[0-9]/.test(password);
        criteria.hasSpecialChar = /[!@#$%&*_\-+=?]/.test(password);
        criteria.isLongEnough = password.length >= 8;
        criteria.hasGoodLength = password.length >= 12;

        if (criteria.hasUpperCase) score++;
        if (criteria.hasLowerCase) score++;
        if (criteria.hasNumbers) score++;
        if (criteria.hasSpecialChar) score++;
        if (criteria.isLongEnough) score++;
        if (criteria.hasGoodLength) score++;

        let strength, strengthClass, details;

        if (score <= 2) {
            strength = "Fraca";
            strengthClass = "strength-weak";
            details = "Adicione mais tipos de caracteres e comprimento";
        } else if (score <= 4) {
            strength = "Média";
            strengthClass = "strength-medium";
            details = "Boa, mas poderia ser mais forte";
        } else {
            strength = "Forte";
            strengthClass = "strength-strong";
            details = "Senha excelente!";
        }

        const criteriaDetails = this.generateCriteriaDetails(criteria);

        return {
            strength: strength,
            class: strengthClass,
            score: score,
            maxScore: 6,
            details: details,
            criteria: criteriaDetails
        };
    }

    /* Criteria Details Generation */
    generateCriteriaDetails(criteria) {
        let details = [];

        if (criteria.hasUpperCase) {
            details.push("✓ Contém letras maiúsculas");
        } else {
            details.push("✗ Adicione letras maiúsculas");
        }

        if (criteria.hasLowerCase) {
            details.push("✓ Contém letras minúsculas");
        } else {
            details.push("✗ Adicione letras minúsculas");
        }

        if (criteria.hasNumbers) {
            details.push("✓ Contém números");
        } else {
            details.push("✗ Adicione números");
        }

        if (criteria.hasSpecialChar) {
            details.push("✓ Contém caracteres especiais");
        } else {
            details.push("✗ Adicione caracteres especiais");
        }

        if (criteria.hasGoodLength) {
            details.push("✓ Comprimento bom (12+ caracteres)");
        } else if (criteria.isLongEnough) {
            details.push("✓ Comprimento mínimo (8+ caracteres)");
        } else {
            details.push("✗ Muito curta (mínimo 8 caracteres)");
        }

        return details;
    }

    /* Strength Indicator Update */
    updateStrengthIndicator(password) {
        try {
            console.log('📊 Updating strength indicator...');

            const strengthContainer = document.querySelector('.password-strength');
            const strengthText = document.getElementById('strengthText');
            const strengthMeter = document.getElementById('strengthMeter');
            const strengthDetails = document.getElementById('strengthDetails');

            if (!strengthContainer || !strengthText || !strengthMeter) {
                console.log('ℹ️ Strength elements not found - ignoring');
                return;
            }

            if (!password) {
                strengthText.textContent = '-';
                strengthMeter.style.width = '0%';
                if (strengthDetails) strengthDetails.innerHTML = '';
                strengthContainer.className = 'password-strength';
                return;
            }

            const strengthInfo = this.checkPasswordStrength(password);

            strengthText.textContent = strengthInfo.strength;
            strengthContainer.className = `password-strength ${strengthInfo.class}`;

            if (strengthInfo.class === 'strength-weak') {
                strengthMeter.style.width = '33%';
            } else if (strengthInfo.class === 'strength-medium') {
                strengthMeter.style.width = '66%';
            } else {
                strengthMeter.style.width = '100%';
            }

            if (strengthDetails && strengthInfo.criteria) {
                strengthDetails.innerHTML = strengthInfo.criteria.map(criteria => {
                    if (criteria.includes('✓')) {
                        return '<div class="strength-criteria criteria-met">' + criteria + '</div>';
                    } else {
                        return '<div class="strength-criteria criteria-missing">' + criteria + '</div>';
                    }
                }).join('');
            }

            console.log('✅ Strength indicator updated!');

        } catch (error) {
            console.error('❌ Error updating indicator:', error);
        }
    }

    /* Password Copy Functionality */
    copyPassword() {
        if (!this.passwordOutput || !this.passwordOutput.value) {
            this.showError('Nenhuma senha para copiar! Gere uma primeiro.');
            this.updateStrengthIndicator('');
            return;
        }

        this.passwordOutput.select();
        this.passwordOutput.setSelectionRange(0, 99999);

        try {
            navigator.clipboard.writeText(this.passwordOutput.value);
            this.showTempMessage('Senha copiada para a área de transferência!', 2000);
        } catch (error) {
            document.execCommand('copy');
            this.showTempMessage('Senha copiada para a área de transferência!', 2000);
        }
    }

    /* Utility Functions */
    setLoading(loading) {
        this.generateBtn.disabled = loading;
        this.generateBtn.textContent = loading ? 'Generating...' : 'Gerar Senha';
    }

    updateLengthDisplay() {
        if (this.passwordLength) {
            this.passwordLength.textContent = `${this.quantityInput.value} characters`;
        }
    }

    showError(message) {
        alert(message);
    }

    showTempMessage(message, duration) {
        const tempDiv = document.createElement('div');
        tempDiv.textContent = message;
        tempDiv.style.cssText = 'position: fixed; top: 20px; right: 20px; background: #27ae60; color: white; padding: 10px 20px; border-radius: 5px; z-index: 1000;';
        document.body.appendChild(tempDiv);

        setTimeout(() => {
            if (tempDiv.parentNode) {
                document.body.removeChild(tempDiv);
            }
        }, duration);
    }
}

/* Application Initialization */
document.addEventListener('DOMContentLoaded', () => {
    console.log('📄 DOM loaded - initializing application...');
    try {
        new PasswordGenerator();
        console.log('🎉 Application initialized successfully!');
    } catch (error) {
        console.error('💥 Error initializing application:', error);
    }
});